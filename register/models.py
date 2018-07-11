from django.db import models
from django.db.models.fields import *

# Create your models here.

class VerifyInfo(models.Model):

    email = EmailField()
    register_code = CharField(max_length=10)
    expired_time = DateTimeField()
    times = IntegerField()