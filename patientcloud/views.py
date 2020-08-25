from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

@login_required
def Index(request):
    return HttpResponse('alright')


def DownloadUpdate(request):
    imgdata = ""
    filepath = "./static/base.apk"
    with open(filepath,'rb') as f:
        imgdata = f.read()
    response = HttpResponse(imgdata,content_type="APPLICATION/OCTET-STREAM")
    response['Content-Disposition'] = 'attachment; filename=base.apk'#设定传输给客户端的文件名称  
    response['Content-Length'] = len(imgdata)

    return response