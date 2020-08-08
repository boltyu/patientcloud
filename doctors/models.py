from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Doctors(User):
    doctorname = models.CharField(null=False,default='None',max_length=64)
    department = models.CharField(null=False,default='None',max_length=64)
