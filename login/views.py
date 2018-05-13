from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
import hashlib

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
    #print(request.session.has_key('cctv'))
    #print(request.session.get("verifycode"))
    
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
    #讲内存中的图片数据返回给客户端,MIME类型为图片png
    return HttpResponse(buf.getvalue(),'image/png')

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
                #print(dir(str_info))
                login_admin.save()

                ##设置session值表示成功登陆过!
                request.session['uid'] = user_info[0].id
                request.session['uname'] = user_info[0].username
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

def getTime():
    from datetime import datetime
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return time

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
    print("cc")
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

                
    
    ##课室查询
    # if request.GET.get(''):
    #     pass
    
    #学科查询
    #if request.GET.get(''):
    #    pass

    

##退出登录
def exit(request):
    del request.session['uid']
    del request.session['uname']

    return JsonResponse({"message":"退出成功!"})



##处理提交过来的数据,并且校验完成之后,就使用多线程或者多进程来处理行为
def estimate_process(request):

    import login.models as L_M
    est_stay_by_info = {}

    infoStr = str(request.POST)
    #具体教学区
    block = is_number(request.POST.get('block'))
    #block = L_M.PortType
    #具体课室
    place = is_number(request.POST.get('place'))

    #详细评价
    typeDetail = is_number(request.POST.get('typeDetail'))
    
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
    ##检验信息的有效性
    if type_1:
        if typeDetail_1:
            if user_name:
                if password:
                    if subject:
                        if block:
                            if place:
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

    port_type = login.models.PortType.objects.filter(id=type)
    est_stay_by_info['type_port'] = port_type[0].port
    
    #获取评价种类具体名称-关键-例如是java基础对应是java-jichu文件
    est_stay_by_info['type_name'] = port_type[0].rname if port_type[0].rname else login.models.PortType.objects.filter(id=typeDetail)

    #虽然拿到了初始化端口,但是,并不是表示可以直接使用!.还是需要对比当前有没有被占用.!
    #但是暂时不做细节!直接用来当启动.!

    estimatingInfo = get_running_node()

    ##根据上面已经获取到的信息,整理一下,准备去调用node.js去启动评价程序了.!
    ##关键首先是端口不冲突
    ##
    
    return JsonResponse({'content':infoStr,'estimateInfo':estimatingInfo})
    
#def 

def network_test(request):
    import os
    import re

    x1 = os.popen("netstat -ntlp|grep -E '0.0.0.0:80[6-9][0-9]'").read()
    x2 = x1.split("\n")
    validInfo = [ x  for x in x2 if x ]
    print(validInfo)
    program = []
    if validInfo:
        for x in validInfo:
            info = {}
            port = re.search("0.0.0.0:80\d\d",x)[0].split(":")[1]
            info['port'] = port
            info['pid'] = re.search("\d+/",x)[0].split("/")[0]
            program.append(info)
    print(program)

    return JsonResponse({'content':'CC'})


#检测目前有哪些node在运行
def get_running_node():
    import os
    import re

    x1 = os.popen("netstat -ntlp|grep -E '0.0.0.0:80[6-9][0-9]'").read()
    x2 = x1.split("\n")
    validInfo = [ x  for x in x2 if x ]
    print(validInfo)
    program = []
    if validInfo:
        for x in validInfo:
            info = {}
            port = re.search("0.0.0.0:80\d\d",x)[0].split(":")[1]
            info['port'] = port
            info['pid'] = re.search("\d+/",x)[0].split("/")[0]
            program.append(info)
    return program


#判断是否为数字
def is_number(number):
    try:
        number1 = int(number)
    except Exception as e:
        return False
    
    return number



