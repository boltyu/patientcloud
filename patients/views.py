from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required, permission_required
from patients.models import Patients


# Create your views here.
def Index(request):
    return HttpResponse('alright')
    
@login_required
def Info(request,idnum):
    Patients.objects.all().filter(doctor=)
    if request.method == 'GET':
        
        pass

    elif request.method == 'POST':
        pass

@login_required
def Epos(request,idnum):
    if request.method == 'GET':
        
        pass

    elif request.method == 'POST':
        pass

@login_required
def Pic(request,idnum):
    if request.method == 'GET':
        
        pass

    elif request.method == 'POST':
        pass
