from django.db import models
from django.utils.timezone import now
# Create your models here.

class Patients(models.Model):
    id = models.AutoField(primary_key=True)
    idnum = models.CharField(unique=True,null=False,max_length=17)
    name = models.CharField(null=False,default='None',max_length=64)
    gender = models.CharField(null=True,max_length=8)
    age = models.IntegerField(null=False,default=1)
    doctor = models.CharField(null=False,default='None',max_length=64)
    description = models.CharField(null=True,default='None',max_length=512)
    ddescription = models.CharField(null=False,default='None',max_length=512)
    devicetype = models.CharField(null=False,default='Medtronic',max_length=128)
    surgerytype = models.CharField(null=False,default='None',max_length=128)
    surgerytime = models.DateTimeField(default=now,editable=True)
    surgerypos = models.CharField(null=False,default='',max_length=128)
    imgpath = models.CharField(null=False,default='',max_length=512)
    created = models.DateTimeField(default=now,editable=False)
    modified = models.DateTimeField(auto_now=True,blank=True)

