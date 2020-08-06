from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Department(models.Model):
    id = models.IntegerField(default=64,primary_key=True)
    name = models.CharField(null=False,default='None',max_length=128)


class Doctors(User):
    doctorname = models.CharField(null=False,default='None',max_length=64)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
