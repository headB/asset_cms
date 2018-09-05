from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse,StreamingHttpResponse,FileResponse
import hashlib
from login.common_func import *
import re


## 公用变量
network_end_ip_list = ['0','64','32']
network_mask_list = ['127','191','223']


##获取通用ip来用来获取设置选项..
common_ip = False

##反正全局变量并没有被调用....所以,,,保险点还是做成函数算了.
def reflash_common_ip():
    from login.models import FrontEndShow
    common_ip_info = FrontEndShow.objects.all()
    
    if not common_ip_info:
        raise ValueError("请先配置数据库中FrontEndShow里面的详细数据,如果为空请填入数据,例如学生访问的页面是192.168.113.1,你就填写ip为192.168.113.1,端口为80就可以了.!")
    else:
        common_ip1 = str(common_ip_info[0].ip)
        global common_ip
        common_ip = common_ip1




reflash_common_ip()


#from django.http import request

# Create your views here.

#import this module for creating verify code
from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
import math,string

##导入model
import login.models


##登陆成功的第一个页面
def index(request):
    
    from .models import FrontEndShow,Location
    # if not request.session.get('uid'):
    #     return redirect('/estimate/login/')
    location_info = FrontEndShow.objects.all()[0]
    if not location_info:
        raise ValueError("没有获取到当前站点信息,请联系系统管理员设置数据库的FrontEndshow数据表")

    ##这个时候应该是关联性查询,不过应该是大批量才对的.

    ##对了,这里可以使用自关联的查询方式
    location_id = location_info.location.id
    location_name = location_info.location.location_name
    location_names = Location.objects.filter(tid=location_id)


    info = {}
    info['uid'] = request.session.get('uid')
    info['uname'] = request.session.get('uname')
    info['title'] = "教学通用信息管理系统"
    info['location_name'] = location_name
    info['locations'] = location_names


    return render(request,'estimate/estimate_index.html',info)
        
##登录页面
def login_index(request):
    
    return render(request,'login/index.html')
##选择页面
def choice_server(request):

    return render(request,'index.html')

def forward_to_estimate(request):
    #return render(request,'index.html')
    return redirect('/estimate/index')

#定义验证码
def verify_code(request):
    verify_object = generate_verify_code(request)
    #讲内存中的图片数据返回给客户端,MIME类型为图片png
    return HttpResponse(verify_object.getvalue(),'image/png')

##验证登录的所有信息
##包括账号密码
def check_login(request):
    
    p_username = request.POST.get('username')
    p_passwd = request.POST.get('password')
    p_verify_code = request.POST.get('codeImage').lower()
    #将传过来的post里面的验证码全部小写化
    verify_code = request.session['verifycode'].lower()

    context = {"title":'登陆',"username":p_username,"password":p_passwd,'verify_code':p_verify_code}

    #将传过来的post里面的验证码全部小写化
    context['session_verify_code'] = verify_code

    #md5_passwd = hashlib.md5((p_passwd+"wolfcodeDTE").encode())
    
    #加盐处理
    #context['md5_passwd'] = md5_passwd.hexdigest()

    user_info = login.models.Admin.objects.filter(username=p_username)
    
    #验证过程
    if verify_code == p_verify_code:
        if user_info:
            p_passwd = hashlib.md5(p_passwd.encode()).hexdigest()
            if p_passwd == user_info[0].password:
                login_admin = login.models.Admin.objects.get(username=p_username)
                login_admin.last_login_time = getTime()
                login_admin.last_login_ip = request.META['REMOTE_ADDR']
                str_info = str(login_admin)
                login_admin.save()

                ##设置session值表示成功登陆过!
                request.session['uid'] = user_info[0].id
                request.session['uname'] = user_info[0].username
                request.session['pid'] = user_info[0].department
                request.session.set_expiry(60*60*12)

                #return HttpResponse("验证成功，这些信息都是你的%s"%str_info)
                return JsonResponse({"message":'成功!','operate':'True'})
            else:
                return JsonResponse({"message":"密码错误！","opreate":"False"})
        else:
            return JsonResponse({"message":"用户不存在！","opreate":"False"})
    else:
        return JsonResponse({"message":"验证码错误","opreate":"False"})
    ##获取当前时间



##展示注册页面
def register(request):

    return render(request,'login/register.html')

##处理注册信息
def register_handle(request):
    p_username = request.POST['username']
    p_password = request.POST['password']
    p_email = request.POST['email']
    p_verify_code = request.POST['verify_code'].lower()

    if p_verify_code == request.session['verifycode'].lower():
        if p_username:
            if p_password:
                p_password = hashlib.md5(p_password.encode()).hexdigest()
                if p_email:
                    newUser = login.models.Admin()
                    newUser.username = p_username
                    newUser.password = p_password
                    newUser.email = p_email
                    #newUser.save()
                    try:
                        newUser.save()
                    except Exception  as e:
                        return JsonResponse({"401":"数据保存失败"})
                    else:
                        return JsonResponse({"202":"数据保存成功"})
                else:
                    return JsonResponse({"403":"没有邮件信息"})
            else:
                return JsonResponse({"405":"没有设置密码"})
        else:
            return JsonResponse({"406":'没有设置用户名'})
    else:
        return JsonResponse({"407":"验证码错误！"})


##ajax,返回该用户名是否被注册
def ajax_handle(request):
    username = request.GET.get('username')
    if username:
        if login.models.Admin.objects.filter(username=username):
            return JsonResponse({"valid":False})
        else:
            return JsonResponse({"valid":True})

    verify_code = request.GET['verify_code']
    
    if verify_code.lower() == request.session['verifycode'].lower():
        return JsonResponse({"valid":True})
    else:
        return JsonResponse({"valid":False})


    return HttpResponse("不好意思,这里什么都没有!")

##评价需要用到的相关信息ajax
def ajax_estimate(request):

    ##评价对象类型
    block = request.GET.get('block')
    if block:
        block = is_number(block)
        ##首先判断是不是数字
        if block:
            classRoom = login.models.ClassRoom.objects.filter(block_number=block)
            classInfo = ''
            if classRoom:
                for i in classRoom:
                    classInfo += str(i.id)+":"+i.class_number+";"
                return HttpResponse(classInfo)
            else:
                return HttpResponse()
        else:
            return HttpResponse()
    

    type = request.GET.get("type")
    if type:
        type = is_number(type)
        if type:
            teacherType = login.models.PortType.objects.filter(tid=type)
            if teacherType:
                infos = ''
                for i in teacherType:
                    infos += str(i.id)+":"+i.type+";"
                return HttpResponse(infos)
            else:
                return HttpResponse()
        else:
            return HttpResponse()

##退出登录
def exit(request):
    del request.session['uid']
    del request.session['uname']
    return redirect("/estimate")
    #return JsonResponse({"message":"退出成功!"})

##处理提交过来的数据,并且校验完成之后,就使用多线程或者多进程来处理行为
def estimate_process(request):

    import login.models as L_M
    global est_stay_by_info
    est_stay_by_info = {}

    infoStr = str(request.POST)
    #具体教学区
    block = is_number(request.POST.get('block'))
    #block = L_M.PortType
    #具体课室
    place = is_number(request.POST.get('place'))

    #详细评价
    typeDetail = is_number(request.POST.get('typeDetail'))
    #当时这个课室的总人数
    total = is_number(request.POST.get('total'))
    
    #被评价人的名字
    user_name = request.POST.get('user_name')
    #评价的班级
    password = request.POST.get('password')
    ##具体学科
    subject = is_number(request.POST.get('subject'))

    #评价种类
    ##根据评价种类,去获取需要启动什么端口,走!
    type = is_number(request.POST.get('type'))
    

    ##全部输入的信息都不能缺少!!
    post_val = block and place and typeDetail and user_name and password and subject
    if post_val:
        pass
    else:
        return JsonResponse({"lack of keyWord Error:":str(request.POST)})


    typeDetail_1 = L_M.PortType.objects.filter(id=typeDetail)
    type_1 = L_M.PortType.objects.filter(id=type)
    place_1 = L_M.ClassRoom.objects.filter(id=place)
    #========================================================#
    ##检验信息的有效性 -------------重要------------------------
    #========================================================#
    if type_1:
        if typeDetail_1:
            if user_name:
                if password:
                    if subject:
                        if block:
                            if place_1:
                                pass
                            else:
                                return JsonResponse({'placeError':"错误"})
                        else:
                            return JsonResponse({'block':"错误"})
                    else:
                        return JsonResponse({'subject':"错误"})
                else:
                    return JsonResponse({'password':"错误"})
            else:
                return JsonResponse({'username':"错误"})
        else:
            return JsonResponse({'typeDetail':"错误"})
    else:
        return JsonResponse({'type':"错误"})

    #==================================================================+
    #重要-----整理所有有效信息去准备调用node启动评价程序!.
    #==================================================================+
    port_type = L_M.PortType.objects.filter(id=typeDetail)
    sort_name = L_M.PortType.objects.filter(id=port_type[0].tid)[0].rname
    est_stay_by_info['type_port'] = L_M.PortType.objects.filter(id=port_type[0].tid)[0].port
    est_stay_by_info['ip'] = place_1[0].ip_addr
    est_stay_by_info['acl'] = place_1[0].ACL
    est_stay_by_info['teacher'] = user_name
    est_stay_by_info['class_name'] = password
    est_stay_by_info['class_room_name'] = place
    est_stay_by_info['total'] = total
    est_stay_by_info['subject'] = subject
    est_stay_by_info['type_detail'] = typeDetail
    est_stay_by_info['who'] = request.session['uname']
    est_stay_by_info['who_id'] = request.session['uid']


    #==================================================================+
    #重要-----#循环判断这个这个端口有没有被暂用
    #==================================================================+

    
    #获取评价种类具体名称-关键-例如是java基础对应是java-jichu文件
    est_stay_by_info['type_name'] = port_type[0].rname if port_type[0].rname else sort_name
   
    
    #虽然拿到了初始化端口,但是,并不是表示可以直接使用!.还是需要对比当前有没有被占用.!
    #但是暂时不做细节!直接用来当启动.!

    #####========================================############==================================
    #####========================================############==================================
    ###超级重要,循环检测端口,看看是否可用!!
    #####========================================############==================================
    #####========================================############==================================
    valid_port = is_used_port(est_stay_by_info['type_port'])
    est_stay_by_info['type_port'] = valid_port


    ##根据上面已经获取到的信息,整理一下,准备去调用node.js去启动评价程序了.!
    ##关键首先是端口不冲突
    generate_config(est_stay_by_info)
    start_estimate(valid_port)

    #####======================================================
    ##最后一步就是设置评价信息到node.js(POST)
    message = set_estimating(est_stay_by_info)
    #####======================================================

    ##简单的判断
    if "teacherName" in message['data']:
        est_stay_by_info['class_info_id'] = message['data']['classInfoId']

        ##记录评价操作到数据库保存作为历史记录
        log_estimate(est_stay_by_info)

        ##然后把刚刚设置的评价,再插入一些必要的信息!,例如是创建者和种类到具体的sqlite3数据库
        insert_in_sqlite3(est_stay_by_info['class_info_id'],sort_name,typeDetail,est_stay_by_info['who_id'])

        ##更新一下所有评价输出静态页面
        show()

        #return HttpResponse("评价成功!被评价老师:%s,评价班级%s"%(message['data']['teacherName'],message['data']['className']))
        return redirect("/estimate/index/manageEstimating")
    else:
        return HttpResponse("评价失败!")

    #经过上面的准备,已经启动好了一个nodejs程序了,然后现在使用curl的模式去提交请求!
    #首先是先生成配置文件,然后执行start_estimate
    
    
    return JsonResponse({'content':infoStr,'prepare_info':str(est_stay_by_info)})

##正在评价的对象
def what_estimating(request):
    show()
    import os
    from datetime import datetime
    import pytz
    SH = pytz.timezone("Asia/Shanghai")
    now = datetime.now(SH)
    #查询到整体
    estimating = login.models.EstimateHistory.objects.filter(is_stop=False)

    ##获取课室信息!
    classRoomInfo = login.models.ClassRoom.objects.all()

    ##整合课室信息!
    classRoomCollect = {}
    for x in classRoomInfo:
        classRoomCollect[x.id] = x.ip_addr
    
    type = login.models.PortType.objects.all()

    detail_type = {}

    for x in type:
        detail_type[x.id] = x.type

    est_dict = {}

    #est_dict['class_info'] = classRoomCollect
    

    est_dict['info'] = []

    #检查有没有多余的端口
    run_est_info = get_running_node_dict()

    ##因为《正在评价》里面有一个实时评价选项，所以必须开启端口。例如80XX的某些通用端口。
    ##获取总分类的端口先。
    top_sort_ports = type.filter(tid=0)
    for x in  top_sort_ports:
        if str(x.port) not in run_est_info:
            info1 = {}
            ##每次都生成配置文件!. 
            info1['type_name'] = x.rname
            info1['type_port'] = x.port
            info1['ip'] = '113'
            generate_config(info1)
            start_estimate(x.port)

    for x in estimating:

        if str(x.port) in run_est_info:
            if x.expired_time > now:
                ##过滤属于自己设置的评价条目
                if x.who_id == request.session.get("uid"):
                    x.type_details = detail_type[x.type_detail]
                    x.class_room_name = classRoomCollect[int(x.class_room_name)]
                    est_dict['info'].append(x)
                    del run_est_info[str(x.port)]
                ##到了这一步,所以不是属于自己,但是也不能把别人正在运行
                ##的评价关闭,所以这里也是需要需要取消加入待强制关闭名单
                else:

                    del run_est_info[str(x.port)]
            else:
                print("kill 419")
                login.models.EstimateHistory.objects.filter(class_info_id=x.class_info_id).update(is_stop=True)
        else:
            print("kill 422")
            login.models.EstimateHistory.objects.filter(class_info_id=x.class_info_id).update(is_stop=True)


    ##然后去调用函数，去查看实时的评价运行情况
    #直接对比端口就好了.
    for x in run_est_info:
        os.system("kill %s"%run_est_info[x])
    
    est_dict['title'] = "当前评价"
    est_dict['uname'] = request.session.get("uname")

    front_end_info = login.models.FrontEndShow.objects.all()
    if front_end_info:
        est_dict['show_address'] = str(front_end_info[0].ip)+":"+str(front_end_info[0].port)
    else:
        est_dict['show_address'] = False
    
    return render(request,'estimate/estimate_manage.html',est_dict)

##历史评价
def export_data(request):
    from datetime import datetime
    est_dict = {}

    est_dict['title'] = "当前评价"
    est_dict['uname'] = request.session.get("uname")

    type_detail = request.GET.get("port")
    if type_detail and type_detail in ("讲师",'班主任','辅导员'):
        est_dict['is_choice'] = True
        if type_detail == "讲师":
            detail = 1
        elif type_detail == "班主任":
            detail = 2
        elif type_detail == "辅导员":
            detail = 3
            
    else:
        est_dict['is_choice'] = False
        return render(request,'estimate/export.html',est_dict)
    
    ##经过上面的简单判断之后,现在进入正式读取指定数据库文件去读取数据了,看看有没有sqlite的驱动先.
    from login.models import PortType
    detail_type = PortType.objects.filter(id=detail)
    est_dict['type_port'] = detail_type[0].rname
    est_dict['class_info_1'] = open_sqlite(est_dict['type_port'],request)

    #算出总这次输出结果的总个数
    #total = len(est_dict['class_info_1'])
    est_dict['class_info'] = []

    for x in est_dict['class_info_1']:
        y2 = []
        for y in range(0,len(x)):
            if y == 3:
                time = x[3]/1000
                y2.append(datetime.fromtimestamp(time))
            else:
                y2.append(x[y])
        est_dict['class_info'].append(y2)
    
    return render(request,'estimate/export.html',est_dict)


def stop_estimate_by_url(request):

    from login.models import EstimateHistory

   
    class_info_id = request.GET.get('class_info_id')

    est_info = EstimateHistory.objects.filter(class_info_id=class_info_id)

    port = request.GET.get('port')  
    uid = est_info[0].who_id

    if est_info[0].who_id == uid and est_info[0].class_info_id == class_info_id:
        message = stop_estimate(est_info[0].port)
        if "data" not in message:
            EstimateHistory.objects.filter(class_info_id=class_info_id).update(is_stop=True)
            return redirect("/estimate/index/export/")

    ##剩下的结果都是停止失败!
    return HttpResponse("sorry!失败了.!")


def export_to_text(request):
    import requests
    import time
    import os
    from login.models import PortType

    ##导出数据的关键在于
    ##获取具体的class_info_id
    ##获取具体详细的评价类型
    ##然后开启具体详细的评价类型的端口就可以了.!

    #首先获取该具体详细的评分类别
    ##然后再获取该评分类型的上一级总类型

    ##先获取数据集
    port_type_a = PortType.objects.all()

    class_info_id = request.GET.get("class_info_id")
    type_detail = is_number(request.GET.get("type_detail"))
    teacher_name = request.GET.get("teacher_name")
    class_name = request.GET.get("class_name")
    date = request.GET.get("date")

    if not (class_info_id and type_detail):
        return JsonResponse({"message":"errorPost"})

    #获取到详细分类==========>用于配合指定模板来导出数据
    detail_a = port_type_a.filter(id=type_detail)

    ##判断出最终用于导出模板分类
    detail_sort = detail_a[0].rname if detail_a[0].rname else port_type_a.filter(id=detail_a[0].tid)[0].rname
    #获取总分类,用于开启具体那种类型来启动程序
    detail_top_sort = port_type_a.filter(id=detail_a[0].tid)
    detail_top_sort = port_type_a.filter(id=detail_a[0].tid) if detail_a[0].tid != 0 else port_type_a.filter(id=detail_a[0].id)
    top_sort_port = str(detail_top_sort[0].port)
    #运行,同样都是需要检测有没有占用...不..直接杀了.!!格杀勿论.
    run_est_info = get_running_node_dict()

    # if top_sort_port in run_est_info:
    #     os.system("kill %s"%run_est_info[top_sort_port])

    ##生成指定配置以提供给程序启动
    start_info = {'type_name':detail_top_sort[0].rname,'type_port':top_sort_port}

    #===========!!!!!!!!!!!!!!!!!!===========================
    ##由于需求问题,然后这里就设置一个假的,随意的ip地址了.!
    start_info['ip'] = '192.168.113'
    #===========!!!!!!!!!!!!!!!!!!===========================

    #检查有没有运行默认的通用端口,没有的话,就运行,否则就不同运行了.!
    if  top_sort_port not in run_est_info:

        generate_config(start_info)
        start_estimate(detail_top_sort[0].port)
        time.sleep(0.8)
    
    ##下面这个链接可以提供给在线查看人数!!
    ##如果通过get请求过来的数据没有时间,就默认只是查看实时的数据

    if not date:
        return_res = requests.get("http://%s:%s/grade/get?id=%s"%(common_ip,detail_top_sort[0].port,class_info_id))
        return HttpResponse(return_res)
    
    
    
    return_res = requests.get("http://%s:%s/grade/download-%s?id=%s"%(common_ip,detail_top_sort[0].port,detail_sort,class_info_id))
    
    from urllib.parse import quote
    the_file_name = quote(teacher_name+"-"+class_name+"-----"+date+".txt")
   
    response = HttpResponse(return_res)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="%s"'%(the_file_name)
    

    return response

##设置一个专门用于给管理员设置一些重要配置的页面
##设置一个专门用于给管理员设置一些重要配置的页面
def admin_setting(request):
    import os
    #print(request.session.get("pid"))
    if request.session.get("pid") != 1:
        return render(request,'estimate/error.html',{'message':'需要网站管理员高级权限','uname':request.session.get('uname')})
    from .models import Location,FrontEndShow,PortType
    location_resource = Location.objects.all()
    admin_setting_resource = FrontEndShow.objects.all()
    amdin_id = admin_setting_resource[0].id

    ##获取所有评价类型的第一个端口.就是默认填写的8081,8091之类的.!
    est_type_info = PortType.objects.filter(tid=0)

    location_info = location_resource.filter(tid=0)
    admin_setting = admin_setting_resource

    block = is_number(request.POST.get('block'))
    ip_addr = request.POST.get('ip_addr')

    dict1 = {}

    res1 = False
    if block and ip_addr:
        
        if location_resource.filter(tid=0,id=block):
            res1 = admin_setting.filter(id=amdin_id).update(location=block,ip=ip_addr)
            if res1:
                dict1['set_success'] = True

                #先更新一下展示ip,然后去获取当前运行的node并且返回
                ##这个是更新common_function模块的common_ip
                reflash_common_ip()

                ##这个是更新这个views模块的common_ip的,这里我学到了就是,更jupyter notebook有点像,就是全局通用.解释性.
                from .common_func.common_function import reflash_common_ip as comm_fun_ip_reflash
                comm_fun_ip_reflash()
                run_node_info = get_running_node_dict()

                ##添加功能.当这里成功设置好新的ip地址之后,就杀掉所有主的80XX这些端口,等待下一次重启.!
            
                for x in est_type_info:
                    if str(x.port) in  run_node_info:
                        os.system("kill -9 %s"%run_node_info[str(x.port)])

                #return redirect("/estimate/admin_setting")
        if not res1: 
            return render(request,'estimate/error.html',{'message':'无法设置成功,请联系网站管理员!','uname':request.session.get('uname')})

    #dict1 = {}
    ##获取所有教学区域
    dict1['location_info'] = location_info
    dict1['admin_setting'] = admin_setting
    dict1['uname'] = request.session.get('uname')

    return render(request,'estimate/admin_setting.html',dict1)

##设置一个专门强制清除多余的node程序的函数,请谨慎使用
def clean_all_node(request):
    import os
    ##如果没有获取到get请求,就展示所有运行中的node
    if request.session.get("pid") != 1:
        return render(request,'estimate/error.html',{'message':'需要网站管理员高级权限','uname':request.session.get('uname')})
    all_run_if = get_all_running_node_dict()
    if request.GET.get("pid"):
        for x in all_run_if:
            os.system("kill -9 %s"%all_run_if[x])
        all_run_if = get_all_running_node_dict()


    return render(request,'estimate/show_all_node.html',{"running_info":all_run_if})


def network_manager(request):
    import ftplib
    import zipfile
    import re
    from .models import ClassRoom,FrontEndShow,Location
    from django.http import HttpResponse 

    from  asset_cms.settings import HOSTNAME,PASSWORD,USERNAME

    f = ftplib.FTP(HOSTNAME) #实例化
    f.login(USERNAME,PASSWORD)

    #获取当前路径
    bufsize = 1024
    fp = open("vrpcfg.zip",'wb')
    f.retrbinary("RETR vrpcfg.zip",fp.write,bufsize)
    fp.close()

    zip_file_target = zipfile.ZipFile("vrpcfg.zip")
    for x in zip_file_target.namelist():
        zip_file_target.extract(x,"vrcfg.txt")
    zip_file_target.close()
    #打开文件
    with open("vrcfg.txt/vrpcfg.cfg") as file1:
        switcher_cfg = file1.readlines()
    #然后是正则提取ACL规则
    switcher_cfg = "".join(switcher_cfg)
    acl_list = re.findall("acl number \d+[\s\S]*?rule.+\n(?! rule)",switcher_cfg)
    #ACL_classification = []
    ACL_classification_dict = {}
    #按分类,保存好规则数据
    for x in acl_list:
        ACL_dict = {}
        ACL_dict['name'] = re.findall("(?<=acl number )\d+",x)[0]
        ACL_dict['rule'] = re.findall("rule.+(?=\n)",x)
        ACL_dict['timer'] = "<span style='color:green'><b>YES</b></span>" if re.findall("time-range",x) else "<span style='color:red'><b>NO</b></span>"
        ACL_dict['online'] = x
        ACL_classification_dict.update({ACL_dict['name']:ACL_dict})
    
    #首先知道当前的教学地点
    try:
        locations = FrontEndShow.objects.all()
        location = Location.objects.filter(tid=locations[0].location_id)
    except Exception as e:
        return HttpResponse("出现严重错误，无法定位当前教学地点")
    #结合当前实际的课室实际的数量来展示数据
    ids = []
    for x in location:
        ids.append(x.id)

    class_room_infos =  ClassRoom.objects.filter(block_number__in=ids)

    ## 尝试循环分类
    #合并两个数据，取合集
    print()
    for x in class_room_infos:
        x.rules = ACL_classification_dict[str(x.ACL)]
        x.state =  judge_network_state(ACL_classification_dict[str(x.ACL)]['online'],x.ip_addr)
        turn_online = re.findall("全部上网",x.state)
        if turn_online:
            x.switch = "offline"
        else:
            x.switch = "online"

    return render(request,"estimate/network.html",{"acl_infos":class_room_infos})


def judge_network_state(acls,network):
    
    """
    :params :acls :传入字符串,并且里面的元素都是字符串类型,作用用于查看这个ACL的具体的规则
    :params :acls :afferent a list which only have string type data
    :params :network :子网段,字需要传入第三位数字,例如 x.x.113.x,你只需要传递113
    """

    #毋庸置疑,必须先定位全局禁止上网的语句的正则语句,这个是全断网,就看位置了
    #这两个优先级别最高，出现谁，情况都是不一样的。
    try:
        global_deny = re.findall("(?<=rule )\d+(?= deny ip \n)",acls)
        global_permit = re.findall("(?<=rule )\d+(?= permit ip \n)",acls)

        global_deny =  int(global_deny[0]) if global_deny else ''
        global_permit =  int(global_permit[0]) if global_permit else ''

        #匹配到局部ip上网
        some_online_rule = re.search("(?<=rule )\d+(?= permit ip source \d+\.\d+\.\d+\.\d+ 0 \n)",acls)
    except Exception as e:
        return "请联系网站技术人员,错误01"

    #然后设定根据当前的ip段,结合规则,看看符不符合上网规则
    #然后,还带自动纠正功能,排列顺序
    try:
        rule_stu_online = common_matching(network,acls)
    except Exception as e:
        return "请联系网站技术人员,错误02"

    #断网正则匹配
    try:
        rule_stu_offline = common_matching(network,acls,operate="deny")
    except Exception as e:
        return "请联系网站技术人员，错误03"
    #然后又设置一段检测是否有安全设置的acl规则
    safe_rule = re.search("(?<=rule )\d+(?= deny ip destination 192\.168\.0.0 0.0\.255\.255)",acls)

    

    #现在关键断不断网，就是看deny和permit是在学生的匹配网段前面还是后面，就知道是否通断网了。
    #先得出学生的规则是否连续，然后取其第一规则的序号
    #上网或者断网，必须空其中一个，才可以继续执行下面的流程
    if  rule_stu_online and rule_stu_offline:
        return "请联系网站技术人员，错误04"

    #处理同时不存在优先级的情况判断,那就剩下
    
    # def jusdge_non_permit_deny():
    #     if 

    #在这里设置障碍，如果都越过了这些障碍，就证明你是可以上网的。不然就是不完整了。

    
    
    break_deny_all = True
    
    deny_all = "<span style='color:red'><b>全部禁网</b></span>"
    permit_all = "<span style='color:green'><b>全部上网</b></span>"
    permit_local = "<span style='color:blue'><b>局部上网，有异常</b></span>"
    deny_local = "<span style='color:blue'><b>局部禁网,有异常</b></span>"

    #处理优先级
    
    #对，处理代码，如果不代入一些事物代表象徵的话，是很难对比的

    def want_to_online(x):
        """
        你想上网的话，就得跨过deny ip 或者 deny ip xxx两个
        """
        break_deny_stu = 3
        state = False
        #看来得超过所有匹配到的才算真正的能上网
        if global_deny:
            if x < global_deny:
                state = True
                return [state,0]
            elif rule_stu_online:
                if rule_stu_online[0] < global_deny:
                    state = True
                    
        if rule_stu_offline:
            if x < rule_stu_offline[-1] and not global_deny:
                state = True

        for y in rule_stu_offline:
            if x < y:
                break_deny_stu -= 1

        if not global_deny and not rule_stu_offline:
            state = True
            break_deny_stu = 0
        
        return [state,break_deny_stu]


    def want_to_offline(x):
        """
        你想断网的话，就得跨过permit ip 或者 permit ip xxx两个
        """
        break_permit_stu = 3
        if global_permit:
            if x > global_permit:
                return False
        
        if rule_stu_online:
            if x > rule_stu_online[0]:
                return False

        return x

    #OK！终于看到，其实中间的处理过程是一样的。就是当两个优先级都不存在的情况
    #优先处理上网

    if global_permit:
        
        x = want_to_online(global_permit)
        if x[0]:      
            if not x[1]:
                return permit_all
            else:
                return permit_local

    if rule_stu_online:
        x = want_to_online(rule_stu_online[-1])
        if x[0]:
            if not x[1]:
                if rule_stu_online.__len__() == 3:
                    return permit_all
        
            return permit_local

    if not global_deny:
        if not rule_stu_offline:
            return "<span style='color:blue'><b>全部凭账号上网</b></span>"
        
    return deny_all
    

def set_network(request):
    import paramiko
    import time
    from  asset_cms.settings import HOSTNAME,PASSWORD,USERNAME
    from .models import ClassRoom

    #然后必须放行服务器段ip
    # :TODO

    #接收get请求,必须的参数是
    #1.课室的id
    #2.操作

    class_id = request.GET.get("cls")
    operate = request.GET.get("operate")

    operate_verify = re.findall("(permit|deny)",operate)
    
    #如果参数不完整,直接跳回网络控制页面
    if not all([class_id,operate]) or not operate_verify:
        return redirect("/estimate/index/network")
    
    #创建ssh对象
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(hostname=HOSTNAME,port=22,username=USERNAME,password=PASSWORD,allow_agent=False,look_for_keys=False)
    except Exception as e:
        return render()

    chan = ssh.invoke_shell()
    # cmds = ['sys\n']
    # res = multi_cmd(chan,cmds)

    #查出课室的id以及他的ACL名字
    try:
        cls_infos = ClassRoom.objects.get(id=int(class_id))
    except Exception as e:
        return render(request,'estimate/fresh.html',{'world':"出现致命错误，交换机链接失败，请2分钟之后再尝试！或者联系技术人员！"})
    
    ip_net = cls_infos.ip_addr

    chan.send("sys\ndis acl %s\n"%cls_infos.ACL)
    time.sleep(0.5)
    res = chan.recv(99999).decode()
    
    #查看具体最高权限的rule序号

    global_deny = re.findall("(?<=rule )\d+(?= deny ip \()",res)
    global_permit = re.findall("(?<=rule )\d+(?= permit ip \()",res)
    global_deny =  int(global_deny[0]) if global_deny else ''
    global_permit =  int(global_permit[0]) if global_permit else ''

    # if global_deny and global_permit:
    #     glo

    rule_stu_online = common_matching(cls_infos.ip_addr,res)
    rule_stu_offline = common_matching(cls_infos.ip_addr,res,operate="deny")

    rule_list = ['100','101','102']

    permit_rules = ''
    deny_rules = ''

    chan.send("acl %s\n"%cls_infos.ACL)

    for x in range(3):
        #修复模式,假如是异常的话
        #设置开启网络的规则
        permit_rules += "rule %s permit ip source 192.168.%s.%s 0.0.0.%s\n"%(rule_list[x],ip_net,network_end_ip_list[x],network_mask_list[x])

    
    for x in range(3):
        #修复模式,假如是异常的话
        #设置开启网络的规则
        deny_rules += "rule %s deny ip source 192.168.%s.%s 0.0.0.%s\n"%(rule_list[x],ip_net,network_end_ip_list[x],network_mask_list[x])


#根据开启还是关闭网络来操作
    if operate == "permit":

        #去除所有断网的语句
        if global_deny:
            chan.send("undo rule %s\n"%global_deny)
        
        for x in rule_stu_offline:
            chan.send("undo rule %s\n"%x)

        for x in rule_stu_online:
            chan.send("undo rule %s\n"%x)
        

        chan.send(permit_rules)

    else:
       #去除所有开网的语句
        if global_permit:
            chan.send("undo rule %s\n"%global_permit)
        
        for x in rule_stu_offline:
            chan.send("undo rule %s\n"%x)

        for x in rule_stu_online:
            chan.send("undo rule %s\n"%x)
        
        
        chan.send(deny_rules)

    time.sleep(2.6)
    res = chan.recv(99999).decode()

    chan.send("dis acl %s\n"%cls_infos.ACL)
    time.sleep(0.7)
    res = chan.recv(9999).decode()
    

    chan.send("q\nq\nsave\ny\n")
    time.sleep(5)
    chan.close()
    rule_stu_online = common_matching(cls_infos.ip_addr,res)
    rule_stu_offline = common_matching(cls_infos.ip_addr,res,operate="deny")

    success_world = "信息返回:%s的网络设置成功,如想再次确认,5秒钟之后自动返回刷新"%cls_infos.class_number
    fail_world = "信息返回:%s的网络设置可能失败了,但系可以5秒钟之后查看你的课室是否设置成功"%cls_infos.class_number

    if operate == "permit":
        if rule_stu_online or rule_stu_offline:
            return render(request,'estimate/fresh.html',{'world':success_world})
    
    return render(request,'estimate/fresh.html',{'world':fail_world})


    #用公用函数获取需要设置的具体分别设置第几条rule规则

    #实在没有办法的话,就统一设置100以后的规则
    


def common_matching(net,acls,operate="permit"):

    """
    :paras :net :具体的子网ip地址,取ip的第三段,例如取 x.x.113.x的113
    :paras :operate :传入匹配上网还是禁止上网的规则,默认是匹配上网的规则
    :paras :acls :传入整句的acl规则,只需要字符串类型数据 
    """

    # rule_list = rule_list
    #匹配学生上网,返回两个参数,一个是rule,一个是是否匹配,所以上面会传入的.
    rules = []
    for x in range(3):
        rule_regex = "(?<=rule )\d+(?= %s ip source 192\.168\.%s\.%s 0\.0\.0\.%s)"%(operate,net,network_end_ip_list[x],network_mask_list[x])
        rule = re.findall(rule_regex,acls)
        try:
            rules.append(int(rule[0])) if rule else ''
        except Exception as e:
            raise ValueError("规则转换出现问题！,请联系网站管理人员")
        
    
    return rules
    
def list_element_to_int(list):
    """
    :paras :list :传入一组数组，然后要求就是里面的元素都是字符串数据类型的数字
    """
    #输入
    pass

def multi_cmd(ssh_object,cmds):
    import time
    for x in cmds:
        ssh_object.send(x)
        time.sleep(0.5)
        res = replace_escape(ssh_object.recv(99999).decode())
        return res

def replace_escape(str):

    return str.replace("---- More ----",'').replace("\x1b[42D",'').replace("  ",'')
