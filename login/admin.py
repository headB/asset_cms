from django.contrib import admin
from login import models
# Register your models here.
class loginAdmin(admin.ModelAdmin):
    list_display = ['username','department','realname']

admin.site.register(models.Admin,loginAdmin)