from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse, Http404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Patients


# Create your views here.
def Index(request):
    return HttpResponse('alright')
    
@login_required
def Info(request,idnum):
    result = {'result':200}
    available_patients = Patients.objects.all().filter(doctorname=request.session['doctorname'],idnum=idnum)
    if available_patients.count == 1:
        patient = available_patients.first()
        if request.method == 'GET':
            result['data'] = patient
        elif request.method == 'POST':#update info
            patient.age = request.POST['info_age']
            patient.ddescription = request.POST['info_ddescription']
            patient.doctor = request.POST['info_doctor']
            patient.description = request.POST['info_description']
            result['result'] = 201
    else:
        if request.mothod == 'POST':
            pass
        else:
            result['result'] = 500    
    return JsonResponse(result)

@login_required
def Epos(request,idnum):
    result = {'result':200}
    available_patients = Patients.objects.all().filter(doctorname=request.session['doctorname'],idnum=idnum)
    if available_patients.count == 1:
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
