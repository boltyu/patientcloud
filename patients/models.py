from django.db import models
from django.utils.timezone import now
# Create your models here.


class Patients(models.Model):
    id = models.AutoField(primary_key=True)
    idnum = models.CharField(unique=True, null=False, max_length=17)

    name = models.CharField(null=False, default='Patient', max_length=64)
    avatar = models.CharField(null=False, default='', max_length=2048)
    gender = models.IntegerField(null=True, default=1)
    birthday = models.DateTimeField(null=False, default=now)
    surgerytime = models.DateTimeField(default=now, editable=True)

    # 手术中心
    surgerycenter = models.CharField(null=False, default='', max_length=128)
    # 术式
    surgerytype = models.IntegerField(null=False, default=1)
    # 设备类型
    devicetype = models.IntegerField(null=False, default=1)
    phone = models.CharField(null=False, default='', max_length=11)

    # 创建该患者的医生id
    doctor = models.IntegerField()
    # 备注
    remark = models.CharField(null=False, default='', max_length=4096)
    # 该条记录是否有效
    valid = models.IntegerField(null=False, default=1)

    created = models.DateTimeField(default=now, editable=False)
    modified = models.DateTimeField(auto_now=True, blank=True)


class Attachment(models.Model):
    # id
    id = models.AutoField(primary_key=True)
    # 患者ID
    pid = models.IntegerField(null=False)
    # 文件名
    filename = models.CharField(null=False, default='', max_length=2048)
    # 文件类型
    # 0: 未定义
    # 1: 头像
    # 2: 病例照片
    # 3: 评估表
    # 4: 电极位置照片
    filetype = models.IntegerField(null=False, default=1)
    # 备注
    remark = models.CharField(null=False, default='', max_length=2048)

'''
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
'''
