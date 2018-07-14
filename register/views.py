from django.shortcuts import render,HttpResponse

# Create your views here.

from django import forms
from django.forms.widgets import PasswordInput,EmailInput,Input,HiddenInput
from django.core.validators import RegexValidator
import pytz
from login.models import Admin
from hashlib import md5


#中国时区
cst = pytz.timezone("Asia/Shanghai")

#验证码大小写通用
def verify_code_common(verify_code):
    #验证码通用四位数 [Aa][Bb][Cc][Dd]
    verify_code_regex = ''
    for x in verify_code:
        verify_code_regex += "["
        verify_code_regex += x.lower()
        verify_code_regex += x.upper()
        verify_code_regex += "]"
    return verify_code_regex

def index(request,url="register/reset.html",operate_name="账户注册"):
    from login.models import Admin
    from register.models import VerifyInfo
    import datetime

    verify_code_regex = ''
    passwd_input_regex = ''
    username_regex = ''
    register_code_regex = ''

    ##用于为验证器提供检查信息,如果有不符合的输入,就自动渲染表单并且返回
    if request.method == "POST": 
        verify_code_regex = verify_code_common(request.session.get('verifycode').lower())
        #组装正则表达式
        #验证码通用四位数 [Aa][Bb][Cc][Dd]
        #设置一个密码的regex，除了需要符合指定格式，还需要两次密码验证正确
        passwd_input_regex = request.POST.get("password")
        is_exist_username = Admin.objects.filter(username=request.POST.get('username'))
        is_exist_register_code = VerifyInfo.objects.filter(email=request.POST.get('email'))
        ##获取当前的用户名，看看有没有冲突/需要添加特殊处理，因为重置密码是需要用户名的
        if is_exist_username:         
            username_regex = is_exist_username[0].username + "111"
        if is_exist_register_code:
            register_code_regex = is_exist_register_code[0].register_code
            
    username_re = "^\w[\w_]{0,20}"
    password_re = '^(?=[\w]*[a-z])(?=[\w]*[A-Z])(?=[\w]*[0-9])\w+'
    email_re = '.+@(wolfcode\.cn|520it\.com)'
 
    class register(forms.Form):
        username = forms.CharField(label='登录名',validators=[RegexValidator(regex=username_re,message="长度不符合或者第一个是非法的空格"),RegexValidator(regex=username_regex,message='用户名已经存在，请换一个！')],max_length=20,widget=Input(attrs={'autocomplete':'off',"placeholder":'支持中文，英文，下划线组合的用户名，空格会被自动过滤'}),error_messages={"required":"该字段不能为空"},)
        password = forms.CharField(label="登陆密码",validators=[RegexValidator(regex=password_re,message="至少包含小写字母+大写字母+数字的密码组合，例如Xm1...,"),RegexValidator('[a-zA-Z0-9]{5,30}',message="不符合最低5位,最大30位的密码要求")],widget=PasswordInput(attrs={'placeholder':'请输入包含至少一个小写字母、大写字母、数字的密码组合，不含空格符'},render_value=True))
        password1 = forms.CharField(label="再次验证密码",validators=[RegexValidator(regex=passwd_input_regex,message="两次密码输入不正确")],widget=PasswordInput(render_value=True))
        email = forms.EmailField(label="请输入你的公司邮箱地址",validators=[RegexValidator(regex=email_re,message='邮箱格式唔岩')],widget=EmailInput(attrs={'placeholder':'请输入xx@520it.com或者xx@wolfcode.cn类似的邮箱','autocomplete':'off'}))
        register_code = forms.CharField(label="注册码",validators=[RegexValidator(regex=register_code_regex,message="注册码错误！")],widget=Input(attrs={'placeholder':'请输入邮箱收到的验证码','autocomplete':'off'})) 
        verify_code = forms.CharField(help_text="点击图片切换验证码",label="验证码",validators=[RegexValidator(verify_code_regex),],widget=Input(attrs={'autocomplete':'off'}),error_messages={"invalid":"验证码错误"},)
    
    class reset(register):
        username = forms.CharField(label='登录名',max_length=20,widget=Input(attrs={'autocomplete':'off',"placeholder":'支持中文，英文，下划线组合的用户名，空格会被自动过滤'}),error_messages={"required":"该字段不能为空"},)
        reset_mark = forms.CharField(required=False,widget=HiddenInput(attrs={'value':"values"}))

    #判断如果接到到post请求,分析是重置密码还是新用户注册
    if request.method == "POST":

        if request.POST.get("reset_mark"):
            register_index = reset(data=request.POST)
        else:
            register_index = register(data=request.POST)

        #到了这一步,如果验证器都通过,再检查一些重要信息之后就可以入库了,否则,这一步通过不了,下面的只是带参数渲染并且返回
        if  register_index.is_valid():
            md5_1 = md5()
            md5_1.update(request.POST.get('password').encode())
            password_valid = md5_1.hexdigest()

            if datetime.datetime.utcnow() < is_exist_register_code[0].expired_time.replace(tzinfo=None):
                if not Admin.objects.filter(email=request.POST.get('email')):
                    x1 = Admin()
                    x1.username = request.POST.get('username')
                    x1.email = request.POST.get('email')
                    x1.department = 20
                    x1.realname = 'xx'
                    x1.password = password_valid
                else:
                    #检测到是存在邮箱,如果同时存在reset_mark就表示重置密码
                    
                    x1 = Admin.objects.get(email=request.POST.get('email'))
                    x1.password = password_valid
                    
            else:
                if Admin.objects.get(email=request.POST.get('email')):
                    return render(request,url,{'form':register_index,"operate_name":"账号密码重置","error":"超时错误!你的注册码冇效,请重新发送注册码到你的邮箱"})          
                else:
                    return render(request,url,{'form':register_index,"operate_name":operate_name,"error":"超时错误!你的注册码冇效,请重新发送注册码到你的邮箱"})          
            #验证都通过的话，尝试一下保存数据
            try:
                x1.save()
            except Exception as e:
                return ValueError("插入数据库错误！")
            if x1.id:
                return render(request,'register/forward.html')
            else:
                return HttpResponse("用户注册失败，请重试或者联系网站管理员！")
    
    ##到了这里,1.可能是新用户注册渲染,2.可能是部分条件不符合带参数渲染返回 3.可能是渲染密码重置的这部分内容,带参数渲染并且返回
    error = ""
    username_disabled = ''
    username_1 = Admin.objects.filter(email=request.GET.get("email"))
    ##
    if request.method == "POST":
        username_1 = Admin.objects.filter(email=request.POST.get('email'))
        if username_1:
            register_index = reset(request.POST)
            operate_name = "账号密码重置"
        else:
            register_index = register(request.POST)
            operate_name = "账号注册"
    else:
        if username_1:
            username_disabled = username_1[0].username
            register_index = reset(request.GET)
            operate_name = "密码重置"
        else:
            register_index = register()
            operate_name = "账号注册"

    return render(request,url,{'form':register_index,"operate_name":operate_name,"username_disabled":username_disabled})


def reset(request):
    message = False
    if request.GET.get('email'):
        message1 =  send_register_code(request,title="密码重置",append_url="cc")
        message = message1.content.decode()
        
    return render(request,'register/reset_passwd.html',{'message':message})
    #index(request,operate_name="密码重置")

##邮件验证码发送！
def send_register_code(request,title=None,append_url=None):
    
    if request.method == 'GET':

        from django.core.mail import send_mail
        from random import randint
        from register.models import  VerifyInfo
        import re
        import datetime

        to_send_who = request.GET.get("email",'')
        email_regex = re.search(".+@(wolfcode\.cn|520it\.com)",to_send_who)
        if "group" not in dir(email_regex):
            return HttpResponse("邮箱错误,请前面的邮箱地址输入xxx@520itcom或者xxx@wolfcode.cn")
        
        check_times = VerifyInfo.objects.filter(email=to_send_who)

        #设置一个普通日期,不带time,只有date

        today = datetime.datetime.utcnow().strftime("%Y-%m-%d")
        x2 = None
        if check_times:
            this_day = check_times[0].expired_time.replace(tzinfo=None).strftime("%Y-%m-%d")
            if today != this_day:
                x2 = VerifyInfo.objects.get(email=to_send_who)
                x2.expired_time = datetime.datetime.now()+datetime.timedelta(minutes=15)
                x2.times = 0
                x2.save()
           
            if not x2:

                if check_times[0].times > 2:
                    return HttpResponse("发送达到极限")

            insert_times = VerifyInfo.objects.get(email=to_send_who)
            insert_times.times = insert_times.times+1
        
        else:
            ##没有发送记录,就创建新的记录
            insert_times = VerifyInfo()
            insert_times.email = to_send_who
            insert_times.times = 1
        
        code_str = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
        random_code = ''
        for x in range(6):
            random_code += code_str[randint(0,len(code_str)-1)]

        ##把注册码保存到数据库
        insert_times.register_code = random_code

        if append_url != None:
            random_code = "http://gz.520langma.com:82/register/?email=%s&register_code=%s"%(to_send_who,random_code)

        #接收post过来的信息，例如是邮件地址，
        to_list = ['lizhixuan@wolfcode.cn',]
        if title == None:
            title = "小码哥/叩丁狼评价系统-注册码"

        content = """这是注册老师评价系统的注册/重置码:%s
        注意：该链接到达你邮箱以后30分钟之内操作有效，超时无效，
        需要重新申请如果你没有申请用户注册码，你可以忽略该邮件，
        对你产生的干扰我们深感抱歉。

    技术支持POWER BY ©Canton wolfcode beetle，如有疑问可以直接回复邮件。
    """%random_code

        x1 = Admin.objects.filter(email=to_send_who)

        if not append_url:

            if x1:

                return  HttpResponse("你现在是重复注册,这是禁止的!")

        else:
        ##到了这一步,要检测是否有记录,如果没有就出错!.
            if not x1:
                return HttpResponse("对不起,你还没有注册,请注册!")


        try:
            x1 = send_mail(title,content,"lizhixuan@wolfcode.cn",[to_send_who,],fail_silently=False)
        except Exception as e:
            return  HttpResponse("发送邮件失败！邮件异常!这个用户并不存在!")
        
        time = (datetime.datetime.now()+datetime.timedelta(minutes=15)).strftime("%Y-%m-%d %H:%M:%S")

        if x1:
            
            insert_times.expired_time = time
            insert_times.save()

            return HttpResponse("发送成功！")

        else:
            return HttpResponse("发送失败！")