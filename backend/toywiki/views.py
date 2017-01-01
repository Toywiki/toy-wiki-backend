from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from backend.settings import MEDIA_ROOT
from uuid import uuid4
from toywiki.utils import Result
import os
# Create your views here.

@csrf_exempt
def upload_img(request):
    result = Result()

    if request.method == "POST":

        img = request.FILES.get("file")
        existingFiles = set(map(lambda str: str.split('.')[0], os.listdir(MEDIA_ROOT) ))
        fileName = str(uuid4())
        while fileName in existingFiles:
            fileName = str(uuid4())


        fileName = fileName + "." + str(img).split(".")[-1]

        #将图片存到media
        with open(os.path.join(MEDIA_ROOT, fileName), "wb") as f:
            for chunk in img.chunks():
                f.write(chunk)

        result.setData("url", "/media/"+fileName)
        result.setOK()

    return HttpResponse(str(result))
