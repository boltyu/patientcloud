from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Doctors
# Create your views here.
@login_required
def Index(request):
    return JsonResponse({'result':200})


def Login(request):
    re = {'result':200}
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request,username=username,password=password)
    
    if user is not None:
        doctor = Doctors.objects.get(pk=user.pk)
        login(request,user)
        request.session['doctor'] = doctor.doctorname
        
    else:
        re['result'] = 500
    return JsonResponse(re)

def Logout(request):
    logout(request)
    return JsonResponse({'result':200})