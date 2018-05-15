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

#课室的信息
class ClassRoom(models.Model):
    class_number = models.CharField(max_length=10)
    block_number = models.IntegerField()
    ip_addr = models.CharField(max_length=80)
    ACL = models.CharField(max_length=20)

##评价对象的分类
class PortType(models.Model):
    tid = models.IntegerField()
    type = models.CharField(max_length=50)
    port = models.IntegerField(null=True)
    rname = models.CharField(max_length=50,null=True)

##学科对象的分类
class SubjectDetail(models.Model):
    tid = models.IntegerField()
    subject_name = models.CharField(max_length=50)
    subject_teacher_name = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=50)

##评价历史
class EstimateHistory(models.Model):
    sid = models.IntegerField()
    who = models.CharField(max_length=20)
    who_id = models.IntegerField(default=-1)
    port = models.IntegerField()
    type_detail = models.IntegerField()
    setting_time = models.DateTimeField()
    expired_time = models.DateTimeField()
    class_info_id = models.CharField(max_length=200)
    class_room_name = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)
    total = models.CharField(max_length=20)
    is_stop = models.CharField(max_length=20,default=False)
    
