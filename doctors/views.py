from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Doctors
# Create your views here.



@login_required
def Index(request):
    return JsonResponse({'result':200})

def PageLogin(request):
    return render(request,"html/login.html")

def Upload(request):
    return render(request,"html/upload.html")

def Login(request):
    re = {'result':200}
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request,username=username,password=password)
    
    if user is not None:
        login(request,user)
        request.session['doctor'] = user.pk
        
    else:
        re['result'] = 500
    return JsonResponse(re)

def Logout(request):
    logout(request)
    return JsonResponse({'result':200})