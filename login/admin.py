from django.contrib import admin
from login import models
# Register your models here.
class loginAdmin(admin.ModelAdmin):
    list_display = ['id','username','department','realname']

class ClassRoom(admin.ModelAdmin):
    list_display = ['id','class_number','block_number','ip_addr','ACL']

class PortTypeAdmin(admin.ModelAdmin):
    list_display = ['id','tid','type','port','rname']

class SubjectDeatailAdmin(admin.ModelAdmin):
    list_display = ['id','tid','subject_name','subject_teacher_name','description']

class EstimateHistoryAdmin(admin.ModelAdmin):
    list_display = ['id','teacher_name','class_name','total','setting_time','expired_time','is_stop','send_email','who']

class LocationAdmin(admin.ModelAdmin):
    list_display = ['id','tid','location_name','description']

admin.site.register(models.Admin,loginAdmin)
admin.site.register(models.ClassRoom,ClassRoom)
admin.site.register(models.PortType,PortTypeAdmin)
admin.site.register(models.SubjectDetail,SubjectDeatailAdmin)
admin.site.register(models.EstimateHistory,EstimateHistoryAdmin)
admin.site.register(models.FrontEndShow)
admin.site.register(models.Location,LocationAdmin)