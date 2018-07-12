from django.contrib import admin

# Register your models here.
from register import models

#class RegisterCode(admin.ModelAdmin):

admin.site.register(models.VerifyInfo)

