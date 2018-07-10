from django.shortcuts import render,HttpResponse

# Create your views here.

from django import forms
from django.forms.widgets import PasswordInput,EmailInput,Input

def index(request):

    class register(forms.Form):
        username = forms.CharField(label='登录名',max_length=20,error_messages={"min_length":"最短为5个字符","required":"该字段不能为空",'autocomplete':'off'},)
        password = forms.CharField(label="登陆密码",widget=PasswordInput(attrs={'placeholder':'请输入包含至少一个小写字母、大写字母、数字的密码组合'},render_value=True))
        password1 = forms.CharField(label="再次验证密码",widget=PasswordInput(render_value=True))
        email = forms.EmailField(label="请输入你的公司邮箱地址",widget=EmailInput(attrs={'placeholder':'请输入xx@520it.com或者xx@wolfcode.cn类似的邮箱','autocomplete':'off'}))
        register_code = forms.CharField(label="注册码",required=False,widget=Input(attrs={'placeholder':'请输入邮箱收到的验证码','autocomplete':'off'}))
        
        verify_code = forms.CharField(label="验证码",widget=Input(attrs={'autocomplete':'off'}))
        
        

    if request.method == "POST":

        register_index = register(data=request.POST)
    else:

        register_index = register()


    return render(request,'register/reset.html',{'form':register_index})
