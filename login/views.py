from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse,StreamingHttpResponse,FileResponse
import hashlib
from login.common_func import *

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
    
    if not request.session.get('uid'):
        return redirect('/estimate/login/')


    info = {}
    info['uid'] = request.session.get('uid')
    info['uname'] = request.session.get('uname')
    info['title'] = "评价首页测试"
    return render(request,'estimate/estimate_index.html',info)
        
##登录页面
def login_index(request):

    return render(request,'login/index.html')

def forward_to_estimate(request):

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
                return redirect('../')
            else:
                return HttpResponse("密码错误！")
        else:
            return HttpResponse("用户不存在！")
    else:
        return HttpResponse("验证码错误")

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
                    newUser.save()
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

    return JsonResponse({"message":"退出成功!"})

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

        return HttpResponse("评价成功!被评价老师:%s,评价班级%s"%(message['data']['teacherName'],message['data']['className']))
    else:
        return HttpResponse("评价失败!")

    #经过上面的准备,已经启动好了一个nodejs程序了,然后现在使用curl的模式去提交请求!
    #首先是先生成配置文件,然后执行start_estimate
    
    
    return JsonResponse({'content':infoStr,'prepare_info':str(est_stay_by_info)})

##正在评价的对象
def what_estimating(request):
    import os
    from datetime import datetime
    import pytz
    SH = pytz.timezone("Asia/Shanghai")
    now = datetime.now(SH)
    #查询到整体
    estimating = login.models.EstimateHistory.objects.filter(is_stop=False)

    type = login.models.PortType.objects.all()

    detail_type = {}

    for x in type:
        detail_type[x.id] = x.type

    est_dict = {}
    est_dict['info'] = []

    #检查有没有多余的端口
    run_est_info = get_running_node_dict()
    

    for x in estimating:

        if str(x.port) in run_est_info:
            if x.expired_time > now:
                ##过滤属于自己设置的评价条目
                if x.who_id == request.session.get("uid"):
                    x.type_details = detail_type[x.type_detail]
                    est_dict['info'].append(x)
                    del run_est_info[str(x.port)]
                ##到了这一步,所以不是属于自己,但是也不能把别人正在运行
                ##的评价关闭,所以这里也是需要需要取消加入待强制关闭名单
                else:

                    del run_est_info[str(x.port)]
            else:
                login.models.EstimateHistory.objects.filter(class_info_id=x.class_info_id).update(is_stop=True)
        else:
            login.models.EstimateHistory.objects.filter(class_info_id=x.class_info_id).update(is_stop=True)


    ##然后去调用函数，去查看实时的评价运行情况
    #直接对比端口就好了.
    for x in run_est_info:
        os.system("kill %s"%run_est_info[x])
    
    est_dict['title'] = "当前评价"
    est_dict['uname'] = request.session.get("uname")
    
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
            return HttpResponse("成功!")

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
    top_sort_port = str(detail_top_sort[0].port)
    #运行,同样都是需要检测有没有占用...不..直接杀了.!!格杀勿论.
    run_est_info = get_running_node_dict()

    # if top_sort_port in run_est_info:
    #     os.system("kill %s"%run_est_info[top_sort_port])

    ##生成指定配置以提供给程序启动
    start_info = {'type_name':detail_top_sort[0].rname,'type_port':top_sort_port}

    #检查有没有运行默认的通用端口,没有的话,就运行,否则就不同运行了.!
    if  top_sort_port not in run_est_info:
        generate_config(start_info)
        start_estimate(detail_top_sort[0].port)
        time.sleep(0.8)
    
    ##下面这个链接可以提供给在线查看人数!!
    ##如果通过get请求过来的数据没有时间,就默认只是查看实时的数据
    if not date:
        return_res = requests.get("http://127.0.0.1:%s/grade/get?id=%s"%(detail_top_sort[0].port,class_info_id))
        return HttpResponse(return_res)
    
    
    
    return_res = requests.get("http://127.0.0.1:%s/grade/download-%s?id=%s"%(detail_top_sort[0].port,detail_sort,class_info_id))
    #print("http://127.0.0.1:%s/grade/download-%s?id=%s"%(detail_top_sort[0].port,detail_sort,class_info_id))

    ##导入模块准备将中文url格式化
    from urllib.parse import quote
    the_file_name = quote(teacher_name+"-"+class_name+"-----"+date+".txt")
   
    response = HttpResponse(return_res)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="%s"'%(the_file_name)
    

    return response


