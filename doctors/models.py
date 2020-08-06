from django.db import models

# Create your models here.

class Department(models.Model):
    id = models.IntegerField(default=64,primary_key=True)
    name = models.CharField(null=False,default='None',max_length=128)


class Doctors(models.Model):
    id = models.IntegerField(default=11520,primary_key=True)
    name = models.CharField(null=False,default='None',max_length=64)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
