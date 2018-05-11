from django.contrib import admin
from login import models
# Register your models here.
class loginAdmin(admin.ModelAdmin):
    list_display = ['username','department','realname']

class ClassRoom(admin.ModelAdmin):
    list_display = ['class_number','block_number','ip_addr','ACL']

class PortTypeAdmin(admin.ModelAdmin):
    list_display = ['tid','type','port','rname']

class SubjectDeatailAdmin(admin.ModelAdmin):
    list_display = ['tid','subject_name','subject_teacher_name','description']

admin.site.register(models.Admin,loginAdmin)
admin.site.register(models.ClassRoom,ClassRoom)
admin.site.register(models.PortType,PortTypeAdmin)
admin.site.register(models.SubjectDetail,SubjectDeatailAdmin)
