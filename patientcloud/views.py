from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

@login_required
def Index(request):
    return HttpResponse('alright')