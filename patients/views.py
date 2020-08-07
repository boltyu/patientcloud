from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse, Http404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Patients
from django.utils import timezone
import json
import random
# get paitents' list
@login_required
def Index(request):
    result = {'result':200}
    if request.method == 'GET':
        available_patients = Patients.objects.all().filter(doctor=request.session['doctor'])
        patientslist = {}
        for i in available_patients:
            patientslist[i.idnum] = {'name':i.name,'gender':i.gender,'age':i.age}
        result['data'] = patientslist
    elif request.method == 'POST':
        try:
            patient = Patients.objects.create(
                idnum=timezone.datetime.now().strftime("%Y%m%d%H%M%S")+str(random.randrange(100,999,1)),
                name=request.POST['name'],
                gender=request.POST['gender'],
                age=request.POST['age'],
                doctor=request.session['doctor'],
                ddescription=request.POST['ddescription'],
                devicetype=request.POST['devicetype'],
                surgerytype=request.POST['surgerytype'],
                surgerytime=timezone.datetime.strptime(request.POST['surgerytime'],"%Y%m%d %H:%M"),
                surgerypos=request.POST['surgerypos'])
            if patient is None:
                result['result':500]
        except Exception(e):
            result['result':400]
            print(e)
    return JsonResponse(result)

@login_required
def Info(request,idnum):
    result = {'result':200}
    available_patients = Patients.objects.all().filter(doctor=request.session['doctor'],idnum=idnum)
    if available_patients.count() == 1:
        patient = available_patients.first()
        if request.method == 'GET':
            patientdata = {
                'name':patient.name,
                'gender':patient.gender,
                'age':patient.age,
                'ddescription':patient.ddescription,
                'devicetype':patient.devicetype,
                'surgerytype':patient.surgerytype,
                'surgerytime':patient.surgerytime.strftime("%Y%m%d %H:%M"),
                'surgerypos':patient.surgerypos
            }
            result['data'] = patientdata
        elif request.method == 'POST':#update info
            patient.age = request.POST['age']
            patient.name = request.POST['name']
            patient.gender = request.POST['gender']
            patient.ddescription = request.POST['ddescription']
            patient.doctor = request.session['doctor']
            patient.devicetype = request.POST['devicetype']
            patient.surgerytype = request.POST['surgerytype']
            patient.surgerytime = timezone.datetime.strptime(request.POST['surgerytime'],"%Y%m%d %H:%M")
            patient.surgerypos = request.POST['surgerypos']
            patient.save()
    else:
        if request.method == 'POST':
            pass
        else:
            result['result'] = 500 
    #patient = Patients.objects.create()
    return JsonResponse(result)
@login_required
def Epos(request,idnum):
    result = {'result':200}
    available_patients = Patients.objects.all().filter(doctor=request.session['doctor'],idnum=idnum)
    if available_patients.count() == 1:
        patient = available_patients.first()
    else:
        pass
    if request.method == 'GET':
        
        pass

    elif request.method == 'POST':
        pass
    return JsonResponse(result)
@login_required
def Pic(request,idnum):
    available_patients = Patients.objects.all().filter(doctorname=request.session['doctorname'],idnum=idnum)
    if request.method == 'GET':
        
        pass

    elif request.method == 'POST':
        pass
