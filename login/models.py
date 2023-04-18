from django.db import models

# Create your models here.

#验证需要用的账户密码
class Admin(models.Model):

    username = models.CharField(max_length=60,unique=True)
    password = models.CharField(max_length=200)
    department = models.IntegerField(default=1)
    email = models.CharField(max_length=100,null=True)
    realname = models.CharField(max_length=50)
    last_login_time = models.DateTimeField(null=True)
    last_login_ip = models.CharField(max_length=50,null=True)
    weixin_openid = models.CharField(max_length=80,null=False)
    xcx_openid = models.CharField(max_length=100,null=False)
    reset_videocode_request = models.CharField(max_length=200,null=True)
    quick_verify = models.CharField(max_length=100,null=True)


#课室的信息
class ClassRoom(models.Model):
    class_number = models.CharField(max_length=10)
    block_number = models.IntegerField()
    ip_addr = models.CharField(max_length=80)
    ACL = models.CharField(max_length=20)
    interface_id = models.IntegerField()

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
    is_stop = models.BooleanField(default=False)
    send_email = models.BooleanField(default=False)
    


##地点信息,例如是北京,上海,广州
class Location(models.Model):
    tid = models.IntegerField(default=0)
    location_name = models.CharField(max_length=60)
    description = models.CharField(max_length=100)

    ##前端学生页面信息
class FrontEndShow(models.Model):
    ip = models.GenericIPAddressField()
    port = models.IntegerField()
    location = models.ForeignKey(Location,on_delete=models.PROTECT,default=1)
    switch_addr = models.CharField(max_length=255)
    acl_uuid = models.CharField(max_length=255)

#cookie的保存
class IewayCookie(models.Model):
    cookie_value = models.CharField(max_length=200)