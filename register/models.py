from django.db import models
from django.db.models.fields import *

# Create your models here.

class VerifyInfo(models.Model):

    register_code = CharField()
    expired_time = DateTimeField()
    times = IntegerField()