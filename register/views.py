from django.shortcuts import render,HttpResponse

# Create your views here.

from django import forms
from django.forms.widgets import PasswordInput,EmailInput,Input,HiddenInput
from django.core.validators import RegexValidator
import pytz
from login.models import Admin


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

    


    ##导入admin模块
    from login.models import Admin
    from register.models import VerifyInfo
    import datetime

    ##加入get判断，如果有特殊参数要求，比如是给定邮件地址



    if request.method == "POST":
        
        verify_code_regex = verify_code_common(request.session.get('verifycode').lower())
        #组装正则表达式
        #验证码通用四位数 [Aa][Bb][Cc][Dd]
       
        #设置一个密码的regex，除了需要符合指定格式，还需要两次密码验证正确
        passwd_input_regex = request.POST.get("password")

        ##获取当前的用户名，看看有没有冲突/需要添加特殊处理，因为重置密码是需要用户名的
        username = Admin.objects.filter(username=request.POST.get('username'))
        username_regex = ''
        if username:
            
            username_regex = username[0].username + "111"
        else:
            username_regex = ''

        ##获取对应的email地址，把正则传递一下
        register_info = VerifyInfo.objects.filter(email=request.POST.get('email'))
        if register_info:
            register_code_regex = register_info[0].register_code
        
        else:
            ##一条永远匹配不了的正则
            register_code_regex = "^(?=[a-z])(?=[A-Z])(?=[0-9])"

    else:
        verify_code_regex = ''
        passwd_input_regex = ''

        #还有一个问题，就是用户名重复的问题，所以，现在再设置一下。
        username_regex = ''
        register_code_regex = ''



    class register(forms.Form):
        username = forms.CharField(label='登录名',validators=[RegexValidator(regex='^\w[\w_]{0,20}',message="长度不符合或者第一个是非法的空格"),RegexValidator(regex=username_regex,message='用户名已经存在，请换一个！')],max_length=20,widget=Input(attrs={'autocomplete':'off',"placeholder":'支持中文，英文，下划线组合的用户名，空格会被自动过滤'}),error_messages={"required":"该字段不能为空"},)
        password = forms.CharField(label="登陆密码",validators=[RegexValidator('^(?=[\w]*[a-z])(?=[\w]*[A-Z])(?=[\w]*[0-9])\w+',message="至少包含小写字母+大写字母+数字的密码组合，例如Xm1...,"),RegexValidator('[a-zA-Z0-9]{5,30}',message="不符合最低5位,最大30位的密码要求")],widget=PasswordInput(attrs={'placeholder':'请输入包含至少一个小写字母、大写字母、数字的密码组合，不含空格符'},render_value=True))
        password1 = forms.CharField(label="再次验证密码",validators=[RegexValidator(regex=passwd_input_regex,message="两次密码输入不正确")],widget=PasswordInput(render_value=True))
        email = forms.EmailField(label="请输入你的公司邮箱地址",validators=[RegexValidator(regex='.+@(wolfcode\.cn|520it\.com)',message='邮箱格式唔岩')],widget=EmailInput(attrs={'placeholder':'请输入xx@520it.com或者xx@wolfcode.cn类似的邮箱','autocomplete':'off'}))
        register_code = forms.CharField(label="注册码",validators=[RegexValidator(regex=register_code_regex,message="注册码错误！")],widget=Input(attrs={'placeholder':'请输入邮箱收到的验证码','autocomplete':'off'})) 
        verify_code = forms.CharField(help_text="点击图片切换验证码",label="验证码",validators=[RegexValidator(verify_code_regex),],widget=Input(attrs={'autocomplete':'off'}),error_messages={"invalid":"验证码错误"},)
        #time = forms.CharField(validators=[RegexValidator(regex='',message="超时了！")],widget=HiddenInput())
    
    

    if request.method == "POST":

        register_index = register(data=request.POST)

        if  register_index.is_valid():
            
            time = datetime.datetime.utcnow().replace(tzinfo=cst)
            
            if time > register_info[0].expired_time:
                return render(request,url,{'form':register_index,"operate_name":operate_name,"error":"超时错误!你的注册码冇效,请重新发送注册码到你的邮箱"})

            is_meail_exist = Admin.objects.filter(email=request.POST.get('email'))

            if is_meail_exist:
                return render(request,url,{'form':register_index,"operate_name":operate_name,"error":"你现在是重复注册,这是禁止的!"})

            x1 = Admin()
            x1.username = request.POST.get('username')
            x1.email = request.POST.get('email')
            x1.department = 20
            x1.realname = 'xx'
            x1.password = request.POST.get('password')
            
            #验证都通过的话，尝试一下保存数据

            try:
                x1.save()
            except Exception as e:
                return ValueError("插入数据库错误！")

            if x1.id:
                return render(request,'register/forward.html')
            else:
                return HttpResponse("用户注册失败，请重试或者联系网站管理员！")

    else:

        register_index = register()


    return render(request,url,{'form':register_index,"operate_name":operate_name})


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
            random_code = "http://gz.520langma.com:82/register/"

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