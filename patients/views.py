from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse, Http404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Patients, Attachment, SurgeryApproach, DeviceType
from django.utils import timezone
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
import json
import random
import hashlib
import os
from PIL import Image

filetype_toint = {"undefine":0,"avatar":1,"pic":2,"eval":3,"epos":4}


class IndexView(LoginRequiredMixin,View):
    login_url = "/doctor/login?"
    def get(self,request):
        result = {'result',200}
        available_patients = Patients.objects.all().filter(doctor=request.session['doctor'])
        patientslist = {}
        for i in available_patients:
            patientslist[i.idnum] = {'name':i.name,'birthday':i.birthday,'phone':i.phone}
        result['data'] = patientslist
        return JsonResponse(result)
    def post(self,request):
        result = {'result':200}
        try:
            idnum = request.POST['idnum']
        except KeyError:
            idnum = ""
        if idnum == "" or idnum == "None":
            patient = Patients.objects.create(
                idnum=timezone.datetime.now().strftime("%Y%m%d%H%M%S")+str(random.randrange(100,999,1)),
                name=request.POST['name'],
                gender=request.POST['gender'],
                birthday=request.POST['birthday'],
                phone=request.POST['phone'],
                doctor=request.session['doctor'],
                remark=request.POST['remark'],
                devicetype=request.POST['devicetype'],
                surgerytype=request.POST['surgerytype'],
                surgerytime=timezone.datetime.strptime(request.POST['surgerytime'],"%Y-%m-%d %H:%M"),
                surgerycenter=request.POST['surgerycenter'])
            if patient is None:
                result['result'] = 500
        else:
            patient = Patients.objects.get(idnum=idnum)
            attachments = Attachment.objects.all().filter(pid=patient.id)
            for i in attachments:
                i.delete()
            #os.remove 暂不删除文件
            patient.delete()
        return JsonResponse(result)
# 获取患者列表或者提交一名新的患者


# 获取或修改患者idnum的详细信息
@login_required
def Info(request,idnum):
    result = {'result':200}
    try:
        patient = Patients.objects.get(doctor=request.session['doctor'],idnum=idnum)
        if request.method == 'GET':
            patientdata = {
                'phone':patient.phone,
                'name':patient.name,
                'gender':patient.gender,
                'birthday':patient.birthday,
                'remark':patient.remark,
                'devicetype':patient.devicetype,
                'surgerytype':patient.surgerytype,
                'surgerytime':patient.surgerytime.strftime("%Y-%m-%d %H:%M"),
                'surgerycenter':patient.surgerycenter
            }
            result['data'] = patientdata
        elif request.method == 'POST':#update info
            patient.birthday = request.POST['birthday']
            patient.name = request.POST['name']
            patient.gender = request.POST['gender']
            patient.phone = request.POST['phone']
            patient.remark = request.POST['remark']
            patient.doctor = request.session['doctor']
            patient.devicetype = request.POST['devicetype']
            patient.surgerytype = request.POST['surgerytype']
            patient.surgerytime = timezone.datetime.strptime(request.POST['surgerytime'],"%Y-%m-%d %H:%M")
            patient.surgerycenter = request.POST['surgerycenter']
            patient.save()
    except Patients.DoesNotExist:
        result['result'] = 500 
    except Patients.MultipleObjectsReturned:
        result['result'] = 500
    #patient = Patients.objects.create()
    return JsonResponse(result)

# 获取患者idnum名下文件类型为category、文件名称为filename的文件，或者修改此文件的备注，或者删除此文件
@login_required
def Picfile(request,idnum,category,filename):
    try:
        global filetype_toint
        fullfilepath = "patients"+os.path.sep+"media"+os.path.sep+idnum+os.path.sep+category+os.path.sep+filename
        patient = Patients.objects.get(doctor=request.session['doctor'],idnum=idnum)
        if request.method == 'GET':
            imgdata = ""
            with open(fullfilepath,'rb') as f:
                imgdata = f.read()
            return HttpResponse(imgdata,content_type="image/jpeg")
        elif request.method == 'POST':
            result = {'result':200}
            try:
                attachment = Attachment.objects.get(pid=patient.pk,filetype=filetype_toint[category],filename=filename)
                if request.POST['method'] == 'remark':
                    attachment.remark = request.POST['data']
                    attachment.save()
                elif request.POST['method'] == 'delete':
                    os.remove(fullfilepath)
                    attachment.delete()
            except: # include FileNotFoundError
                    result['result'] = 500
            return JsonResponse(result)
    except Patients.DoesNotExist:
        return Http404()
    except Patients.MultipleObjectsReturned:
        print('idnum repeat')
        return Http404()

# 获取患者idnum名下类型为category的文件列表，或向其提交一个文件
@login_required
def Pic(request,idnum,category):
    result = {'result':200,"data":{}}
    try:
        global filetype_toint
        patient = Patients.objects.get(doctor=request.session['doctor'],idnum=idnum)
        if request.method == 'GET':
            attachments = Attachment.objects.all().filter(pid=patient.pk,filetype=filetype_toint[category])
            for i in attachments:
                result['data'][i.filename] = i.remark
        elif request.method == 'POST':# 提交新文件
            #try:
            for fp in request.FILES:
                tmpfile = request.FILES[fp]
                tmptype = tmpfile.name.split('.').pop()
                filedata = b''
                for chunk in tmpfile.chunks():
                    filedata=filedata+chunk
                newname = hashlib.md5(filedata).hexdigest()+"."+tmptype
                filepath = 'patients/media/'+idnum+"/"+category
                MakesureDirExist(filepath)
                fullfilepath = filepath+"/"+newname
                with open(fullfilepath,'wb+') as f:
                    f.write(filedata)
                a = Image.open(fullfilepath)
                a.save(fullfilepath)
                a.close()
                Attachment.objects.create(pid=patient.pk,filename=newname,filetype=filetype_toint[category])
            #except:#catch all ex?
            #    result['result'] = 500
    except Patients.DoesNotExist:
        result['result'] = 503
    except Patients.MultipleObjectsReturned:
        result['result'] = 501 
    except KeyError:
        result['result'] = 502
    except:
        reusul['result'] = 500

    return JsonResponse(result)
        

cache_surgeryapproch = {}
@login_required
def SurgeryApproachList(request):
    result = {'result':200}
    if request.method == "GET":
        listall = SurgeryApproach.objects.all()
        for i in listall:
            cache_surgeryapproch[str(i.id)] = i.name
        result['data'] = cache_surgeryapproch
    elif request.method == 'POST':
        #tmpobj = SurgeryApproach.objects.create()
        pass
    return JsonResponse(result)

cache_devicetype = {}
@login_required
def DeviceTypeList(request):
    result = {'result':200}
    if request.method == "GET":
        listall = DeviceType.objects.all()
        for i in listall:
            cache_devicetype[str(i.id)] = i.name
        result['data'] = cache_devicetype
    elif request.method == 'POST':
        #tmpobj = SurgeryApproach.objects.create()
        pass
    return JsonResponse(result) 



def MakesureDirExist(fullpath):
    try:
        os.makedirs(fullpath)
        return 1
    except FileExistsError:
        return 0
    except:
        return -2
    return -1
