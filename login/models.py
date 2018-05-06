from django.db import models

# Create your models here.

#验证需要用的账户密码
class Admin(models.Model):

    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=200)
    department = models.IntegerField(default=1)
    email = models.CharField(max_length=100,null=True)
    realname = models.CharField(max_length=50)
    last_login_time = models.DateTimeField(null=True)
    last_login_ip = models.CharField(max_length=50,null=True)