from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from backend.settings import MEDIA_ROOT
from toywiki.models import Wiki, WikiUser, Comment, User
from uuid import uuid4
from toywiki.utils import Result
import os
import json
# Create your views here.

@csrf_exempt
def upload_img(request):
    result = Result()

    if request.method == "POST":

        img = request.FILES.get("file")
        existingFiles = set(map(lambda str: str.split('.')[0], os.listdir(MEDIA_ROOT) ))
        filename = str(uuid4())
        while filename in existingFiles:
            filename = str(uuid4())

        filename = filename + "." + str(img).split(".")[-1]

        #将图片存到media
        with open(os.path.join(MEDIA_ROOT, filename), "wb") as f:
            for chunk in img.chunks():
                f.write(chunk)

        result.setData("url", "/media/"+filename)
        result.setOK()

    return HttpResponse(str(result))

@csrf_exempt
def create_wiki(request):
    result = Result()
    if request.method == "POST":
        title = json.loads(request.body.decode()).get('title')

        existing = Wiki.objects.filter(title__icontains=title, status=1).order_by('time')

        if len(existing) > 0:
            result.setStatuscode(1)
            result.setData("existing", [])

            temp = set()

            for i in existing[::-1]:
                if i.title not in temp:
                    result["existing"].append({"title": i.title, "id": i.id, "introduction": i.introduction,
                                           "img": i.img_url})
                    temp.add(i.title)
        else:
            result.setStatuscode(0)

    return HttpResponse(str(result))

@csrf_exempt
def view_wiki(request):
    result = Result()
    if request.method == "GET":
        id = request.GET.get('id')
        wiki = Wiki.objects.filter(id=id)
        if len(wiki) > 0:
            result.setData("title", wiki[0].title)
            result.setData("introduction", wiki[0].introduction)
            result.setData("content", wiki[0].content)
            result.setData("img", wiki[0].img_url)
            result.setOK()

    return HttpResponse(str(result))

@csrf_exempt
def save_wiki(request):
    result = Result()
    if request.method == "POST":
        wiki = json.loads(request.body.decode())
        if wiki is not None:
            account = wiki.get('account')
            title = wiki.get('title')
            introduction = wiki.get('introduction')
            category = wiki.get('category')
            content = wiki.get('content')
            img = wiki.get('img')
            newWiki = Wiki(title=title, introduction=introduction, category=category, content=content, img_url=img, status=0)
            newWiki.save()

            user = User.objects.filter(account=account)[0]
            newWikiUser = WikiUser(user_account=user, wiki=newWiki, relationship=1)
            newWikiUser.save()

            result.setOK()

    return HttpResponse(str(result))

@csrf_exempt
def edit_wiki(request):
    result = Result()
    if request.method == "POST":
        wiki = json.loads(request.body.decode())
        if wiki is not None:
            account = wiki.get('account')
            wiki_id = wiki.get('wiki_id')
            introduction = wiki.get('introduction')
            category = wiki.get('category')
            content = wiki.get('content')
            img = wiki.get('img')

            oldWiki = Wiki.objects.filter(id=wiki_id)[0]

            newWiki = Wiki(title=oldWiki.title, introduction=introduction, category=category, content=content, img_url=img, status=0)
            newWiki.save()

            user = User.objects.filter(account=account)[0]
            newWikiUser = WikiUser(user_account=user, wiki=newWiki, relationship=2)
            newWikiUser.save()

            result.setOK()

    return HttpResponse(str(result))




