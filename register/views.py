from django.shortcuts import render,HttpResponse

# Create your views here.

from django import forms
from django.forms.widgets import PasswordInput,EmailInput,Input
from django.core.validators import RegexValidator

def index(request):

    if request.method == "POST":
        
        verify_code_session = request.session.get('verifycode').lower()
        verify_code_regex = ''
        #组装正则表达式
        for x in verify_code_session:
            verify_code_regex += "["
            verify_code_regex += x.lower()
            verify_code_regex += x.upper()
            verify_code_regex += "]"
            

        #四位数 [Aa][Bb][Cc][Dd]

    else:
        verify_code_regex = ''

    class register(forms.Form):
        username = forms.CharField(label='登录名',max_length=20,widget=Input(attrs={'autocomplete':'off'}),error_messages={"min_length":"最短为5个字符","required":"该字段不能为空"},)
        password = forms.CharField(label="登陆密码",validators=[RegexValidator('^[a-zA-Z]'),RegexValidator('[a-z]+[A-Z]+')],widget=PasswordInput(attrs={'placeholder':'请输入包含至少一个小写字母、大写字母、数字的密码组合'},render_value=True))
        password1 = forms.CharField(label="再次验证密码",widget=PasswordInput(render_value=True))
        email = forms.EmailField(label="请输入你的公司邮箱地址",widget=EmailInput(attrs={'placeholder':'请输入xx@520it.com或者xx@wolfcode.cn类似的邮箱','autocomplete':'off'}))
        register_code = forms.CharField(label="注册码",required=False,widget=Input(attrs={'placeholder':'请输入邮箱收到的验证码','autocomplete':'off'})) 
        verify_code = forms.CharField(help_text="点击图片切换验证码",label="验证码",validators=[RegexValidator(verify_code_regex),],widget=Input(attrs={'autocomplete':'off'}),error_messages={"invalid":"验证码错误"},)
        
        

    if request.method == "POST":

        register_index = register(data=request.POST)

        if  register_index.is_valid():

            return HttpResponse("信息有效")

    else:

        register_index = register()


    return render(request,'register/reset.html',{'form':register_index})
