#判断是否为数字
import os

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
def is_used_port(port_numer):
    estimate_info = get_running_node()
    run_port = {}
    for x in estimate_info:
        run_port[x['port']] = x['pid']

    for x in range(int(port_numer),int(port_numer)+9):
        
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
    
    program_dir = "/home/python/estimate/XMG-estimate/TM2015/bin/www-%s"%port
    os.popen("nohup node %s > /dev/null 2>&1 &"%program_dir)


#检测目前有哪些node在运行
def get_running_node():
    import os
    import re

    x1 = os.popen("netstat -ntlp|grep -E '0.0.0.0:80[6-9][0-9]'").read()
    x2 = x1.split("\n")
    validInfo = [ x  for x in x2 if x ]
    program = []
    if validInfo:
        for x in validInfo:
            info = {}
            port = re.search("0.0.0.0:80\d\d",x)[0].split(":")[1]
            info['port'] = port
            info['pid'] = re.search("\d+/",x)[0].split("/")[0]
            program.append(info)
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

    position = "/home/python/estimate/XMG-estimate/TM2015/bin/www-%s"%est_info['type_port']

    ##写入配置文件到指定位置
    with open(position,'w') as file1:
        file1.write(content)

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
    est_his.port = est_info['type_port']
    est_his.type_detail = est_info['type_detail']
    est_his.setting_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    est_his.expired_time = (datetime.now() + timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S")
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