#判断是否为数字
import os
from django.http import HttpResponse
from .nodejs_items import return_nodejs_security

def is_number(number):
    try:
        number1 = int(number)
    except Exception as e:
        return False
    
    return number

def getTime():
    from datetime import datetime
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return time

#循环判断这个这个端口有没有被暂用,还有就是是否空闲的,直接可以利用的.!
#===========================================##################====================
############注意了,虽然这个过程好像之前的一个地方,不过这个不一样的地方在于,这是只是将目前没有评价的对象杀一次!
#===========================================##################====================
def is_used_port(port_numer):
    run_port = get_running_node_dict()

    for x in range(int(port_numer)+1,int(port_numer)+9):
        
        if str(x) in run_port:
            if is_set_est_info(x):
                #已经被占用,跳到下一个条件继续循环
                pass
            else:
                #把进程结束
                os.system("kill %s"%run_port[str(x)])
                return x
        else:
            return x
    from django.http import HttpResponse
    return HttpResponse("不好意思,端口都使用完了.!")


#这个是用于判断这个已经启动的评价程序对应的端口是否已经设置评价信息
def is_set_est_info(x):
    import requests
    x1 = requests.post("http://127.0.0.1:%s/grade/init"%x).json()
    if "teacherName" not in x1['data']:
        stop_estimate(x)
        return False
    else:
        return x1


##停止评价
def stop_estimate(x):

    import requests

    x1 = requests.post("http://127.0.0.1:%s/grade/commit"%x)
    return  x1.json()

#启动nodejs评价程序
def start_estimate(port):
    
        os.popen("""
cd /home/python/estimate/XMG-estimate/TM2015
nohup node bin/www-%s > /dev/null 2>&1 &
"""%port)
    #program_dir = "/home/python/estimate/XMG-estimate/TM2015/bin/www-%s"%port
    #os.popen("nohup node %s > /dev/null 2>&1 &"%program_dir)


#检测目前有哪些node在运行
def get_running_node_dict():
    import os
    import re

    x1 = os.popen("netstat -ntlp|grep -E '0.0.0.0:80[6-9][0-9]'").read()
    x2 = x1.split("\n")
    validInfo = [ x  for x in x2 if x ]
    program = {}
    if validInfo:
        for x in validInfo:
            info = {}
            port = re.search("0.0.0.0:80\d\d",x)[0].split(":")[1]
            program[port] = re.search("\d+/",x)[0].split("/")[0]
    return program



##===============================================
##================重要!,获取到有效端口之后,需要传入评价信息,先写评价用到的配置列表信息,生成www-80xx===============================
##===============================================

def generate_config(est_info):

    content = """#!/usr/bin/env node
var debug = require('debug')('TM2014');


var fs = require("fs");
process.on("uncaughtException",function(err){
    fs.writeFile("/home/python/nodejs_error_log.txt","err:"+err);
});

var app = require('../app-%s');
app.set('port', process.env.PORT || %s);

var server = app.listen(app.get('port'), function() {
console.log("@启动成功");
console.log("@打开浏览器输入：127.0.0.1: %s 进行使用");
});
            """%(est_info['type_name'],est_info['type_port'],est_info['type_port'])

    position = "/home/python/estimate/XMG-estimate/TM2015/"
    position_www = position+"bin/www-%s"%est_info['type_port']
    position_security = position+"routes/security.js"
    ##写入配置文件到指定位置
    with open(position_www,'w') as file1:
        file1.write(content)

    ##准备生成安全检查的文件
    security_info = return_nodejs_security(est_info['ip'])
    if not security_info:
        return HttpResponse("error!error ip addr")

    with open(position_security,'w') as file2:
        file2.write(security_info)

##定义一个函数去记录评价历史
def log_estimate(est_info):
    from datetime import datetime,timedelta
    #import pytz
    from login.models import EstimateHistory

    #设置好时区
    #tz = pytz.timezone('Asia/Shanghai')

    ##首先给整理好准备插入到数据库的历史记录
    est_his = EstimateHistory()
    est_his.sid = est_info['subject']
    est_his.who = est_info['who']
    est_his.who_id = est_info['who_id']
    est_his.port = est_info['type_port']
    est_his.type_detail = est_info['type_detail']
    est_his.setting_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    est_his.expired_time = (datetime.now() + timedelta(hours=2)).strftime("%Y-%m-%d %H:%M:%S")
    est_his.class_info_id = est_info['class_info_id']
    est_his.class_room_name = est_info['class_room_name']
    est_his.teacher_name = est_info['teacher']
    est_his.class_name = est_info['class_name']
    est_his.total = est_info['total']

    return est_his.save()


def set_estimating(est_info):
    
    import requests
    import time
    time.sleep(0.8)
    estimate_info = {'teacherName':est_info['teacher'],'className':est_info['class_name']}
    lens = len(str(estimate_info))
    header = {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Content-Length': str(lens)}
    x1 = requests.post("http://127.0.0.1:%s/grade/init"%est_info['type_port'],data=estimate_info,headers=header)
    return  x1.json()

##获取具体的评价信息,例如是每一个学生的具体ABCD评价
def open_sqlite_common(type_detail,calss_info_id):
    import sqlite3
    est_db_path = "/home/python/estimate/XMG-estimate/TM2015/db/grade-%s.db"%type_detail
    est_db = sqlite3.connect(est_db_path)
    est_dbCu = est_db.cursor()
    sql = "select * from comment where classInfoId='%s'"%calss_info_id
    est_dbCu.execute(sql)
    res1 = est_dbCu.fetchall()
    est_db.close()
    return res1

##打开Sqlite数据库.
def open_sqlite(type_detail,request):

    import sqlite3
    est_db_path = "/home/python/estimate/XMG-estimate/TM2015/db/grade-%s.db"%type_detail
    est_db = sqlite3.connect(est_db_path)
    est_dbCu = est_db.cursor()

    ##在这里设置权限
    ##以部门+用户id来确定
    pid = request.session.get('pid')
    uid = request.session.get('uid')
    if pid == 1:
        sql = "select * from classinfo order by inputTime DESC limit 25"
    else:
        sql = "select * from classinfo where creator = '%s' order by inputTime DESC limit 25"%uid

    est_dbCu.execute(sql)
    res = est_dbCu.fetchall()
    est_dbCu.close()
    return res

##用于插入信息到sqlite3
def insert_in_sqlite3(class_info_id,sort_name,typeDetail,who):
    import sqlite3
    est_db_path = "/home/python/estimate/XMG-estimate/TM2015/db/grade-%s.db"%sort_name
    est_db = sqlite3.connect(est_db_path)
    est_dbCu = est_db.cursor()
    est_dbCu.execute("update classinfo set creator='%s',typeDetail='%s' where id='%s'"%(who,typeDetail,class_info_id))
    est_db.commit()
    est_db.close()


##日常生成目前能用的评价条目
def check_run_estimate():
    from login.models import EstimateHistory
    ##获取在数据库里面的历史记录(条件为is_stop=False)
    est = EstimateHistory.objects.all()
    est_info = est.filter(is_stop=False)
    run_est_info = get_running_node_dict()
    
    valid_est = []

    for x  in est_info:
        valid_est_dict = {}
        ##晕.....对比字符串的数字和int类型的数字的时候注意了.!!晕...!!.
        if str(x.port) in run_est_info:
            ##如果评价项目运行中,获取班级和讲师名字,还有具体的端口号
            valid_est_dict['teacher_name'] = x.teacher_name
            valid_est_dict['class_name'] = x.class_name
            valid_est_dict['type_port'] = x.port

            #然后把信息保存到字典里面
            valid_est.append(valid_est_dict)
        else:
            #如果已经失效了,就登记为不是有效的实时评价状态.!
            est.filter(id=x.id).update(is_stop=True)
        
        

    ##把有用的信息传递到模板,输出条目
    return valid_est





##产生验证码
def generate_verify_code(request):
    import random
    from PIL import Image,ImageDraw,ImageFont

    bgcolor = (random.randrange(20,100),random.randrange(20,100),100)
    width = 150
    height = 40
    #创建画面对象
    im = Image.new('RGB',(width,height),bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0,100):
        xy = (random.randrange(0,width),random.randrange(0,height))
        fill = (random.randrange(0,255),255,random.randrange(0,255))
        draw.point(xy,fill=fill)

    #定义验证码的备选值
    str1 = 'QWERTYUIOPAShjluiotvcvbmzcvsfcrDFGHJasdKLZXCVBNM1234567890'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0,4):
        rand_str += str1[random.randrange(0,len(str1))]

    #构造字体对象,centos的字体位置
    font = ImageFont.truetype('static/msyh.ttc',25)
    #构造字体颜色
    fontcolor = (255,random.randrange(0,255),random.randrange(0,255))
    #绘制4个字
    draw.text((5,1),rand_str[0],font=font,fill=fontcolor)
    draw.text((35,2),rand_str[1],font=font,fill=fontcolor)
    draw.text((50,3),rand_str[2],font=font,fill=fontcolor)
    draw.text((75,1),rand_str[3],font=font,fill=fontcolor)

    #释放画笔
    del draw

    #存入session,用于提交表单的时候,验证是否非机器人

    request.session['verifycode'] = rand_str
    #内存文件操作

    #python3里面没有cStingIO,改为IO
    import io
    buf = io.BytesIO()
    #将图片保存在内存中,文件类型为png
    im.save(buf,'png')

    return buf


    #获取当前可用的评价条目
def show():


    import os
    from django.template.loader import render_to_string
    #调用公共函数
    from login.models import PortType,FrontEndShow

   
    valid_est_info = check_run_estimate()

    ##调出在数据库中记录的ip地址,前端展示给学生那个

    front_end_info = FrontEndShow.objects.all()

    if not front_end_info:
        raise ValueError("请先配置数据库中FrontEndShow里面的详细数据,如果为空请填入数据,例如学生访问的页面是192.168.113.1,你就填写ip为192.168.113.1,端口为80就可以了.!")

    collections = {}
    for x in valid_est_info:
        collect_detail = {}
        #采用切片的方式,切倒数第二个数进行对比
        #主要是用于快速组合对应的数据.
        coll_port = str(x["type_port"])[0:3]+str(1)

        if coll_port not in collections:
            collections[coll_port] = {'data':[x,]}
        else:
            collections[coll_port]['data'].append(x)
        ##准备用于生成静态资源.!
        
    
        #如果静态文件不存在的话,直接生成====补充=====>是不是都是直接覆盖的....不好意思了.!
        #而且是循环生成---大概都是3次或者4次

    for x in  PortType.objects.filter(tid=0):
        collection = {}
        collection['type'] = x.type  ##中文名
        collection['rname'] = x.rname  ##英文名
        collection['show_address'] = str(front_end_info[0].ip)
        if str(x.port) in collections:
            
            collection['data'] = collections[str(x.port)]['data'] #结果集
        
        static_html = "/home/python/asset_cms/static/student/%s.html"%x.rname
        content = render_to_string('estimate/show.html',collection)
        with open(static_html,'w') as static_file:
            static_file.write(content)
        
            
    

        ##################################
        #管理静态内容的最佳方法是,直接使用django缓存功能.
        #################################于给定的网址，尝试从缓存中找到网址，如果页面在缓存中，直接返回缓存的页面，如果缓存中没有，一系列操作（比如查数据库）后，保存生成的页面内容到缓存系统以供下一次使用，然后返回生成的页面内容。
        ##################################


    #return HttpResponse("生成文件成功!")
    #return render(request,'estimate/show.html',{'valid_est':valid_est_info})