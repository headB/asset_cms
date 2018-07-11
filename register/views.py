from django.shortcuts import render,HttpResponse

# Create your views here.

from django import forms
from django.forms.widgets import PasswordInput,EmailInput,Input
from django.core.validators import RegexValidator

def index(request):

    ##导入admin模块
    from login.models import Admin

    if request.method == "POST":
        
        verify_code_session = request.session.get('verifycode').lower()
        verify_code_regex = ''
        #组装正则表达式
        #验证码通用四位数 [Aa][Bb][Cc][Dd]
        for x in verify_code_session:
            verify_code_regex += "["
            verify_code_regex += x.lower()
            verify_code_regex += x.upper()
            verify_code_regex += "]"
        
        #设置一个密码的regex，除了需要符合指定格式，还需要两次密码验证正确
        passwd_input_regex = request.POST.get("password")

        ##获取当前的用户名，看看有没有冲突
        username = Admin.objects.filter(username=request.POST.get('username'))
        username_regex = ''
        if username:
            
            username_regex = username[0].username + "111"
        else:
            username_regex = ''


    else:
        verify_code_regex = ''
        passwd_input_regex = ''

        #还有一个问题，就是用户名重复的问题，所以，现在再设置一下。
        username_regex = ''


    class register(forms.Form):
        username = forms.CharField(label='登录名',validators=[RegexValidator(regex='^\w[\w_]{0,20}',message="长度不符合或者第一个是非法的空格"),RegexValidator(regex=username_regex,message='用户名已经存在，请换一个！')],max_length=20,widget=Input(attrs={'autocomplete':'off',"placeholder":'支持中文，英文，下划线组合的用户名，空格会被自动过滤'}),error_messages={"required":"该字段不能为空"},)
        password = forms.CharField(label="登陆密码",validators=[RegexValidator('^(?=[\w]*[a-z])(?=[\w]*[A-Z])(?=[\w]*[0-9])\w+',message="至少包含小写字母+大写字母+数字的密码组合，例如Xm1...,"),RegexValidator('[a-zA-Z0-9]{5,30}',message="不符合最低5位,最大30位的密码要求")],widget=PasswordInput(attrs={'placeholder':'请输入包含至少一个小写字母、大写字母、数字的密码组合，不含空格符'},render_value=True))
        password1 = forms.CharField(label="再次验证密码",validators=[RegexValidator(regex=passwd_input_regex,message="两次密码输入不正确")],widget=PasswordInput(render_value=True))
        email = forms.EmailField(label="请输入你的公司邮箱地址",widget=EmailInput(attrs={'placeholder':'请输入xx@520it.com或者xx@wolfcode.cn类似的邮箱','autocomplete':'off'}))
        register_code = forms.CharField(label="注册码",required=False,widget=Input(attrs={'placeholder':'请输入邮箱收到的验证码','autocomplete':'off'})) 
        verify_code = forms.CharField(help_text="点击图片切换验证码",label="验证码",validators=[RegexValidator(verify_code_regex),],widget=Input(attrs={'autocomplete':'off'}),error_messages={"invalid":"验证码错误"},)
        
        

    if request.method == "POST":

        register_index = register(data=request.POST)

        if  register_index.is_valid():
            
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


    return render(request,'register/reset.html',{'form':register_index})


##邮件验证码发送！
def send_register_code(request):
    
    if request.method == 'GET':

        from django.core.mail import send_mail
        from random import randint

        code_str = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
        random_code = ''
        for x in range(6):
            random_code += code_str[randint(0,len(code_str)-1)]

        

        #接收post过来的信息，例如是邮件地址，
        to_list = ['lizhixuan@wolfcode.cn',]

        title = "小码哥/叩丁狼评价系统-注册码"

        content = """这是注册老师评价系统的注册码:%s
        注意：该链接到达你邮箱以后30分钟之内操作有效，超时无效，
        需要重新申请如果你没有申请用户注册码，你可以忽略该邮件，
        对你产生的干扰我们深感抱歉。

    技术支持POWER BY ©Canton wolfcode beetle，如有疑问可以直接回复邮件。
    """%random_code



        x1 = send_mail(title,content,"lizhixuan@wolfcode.cn",to_list,fail_silently=False)
        
        if x1:
            return HttpResponse("发送成功！")
        else:
            return HttpResponse("发送失败！")