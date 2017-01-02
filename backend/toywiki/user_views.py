from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from toywiki.models import User, Wiki, WikiUser
from toywiki.utils import Result
from django.db.models import F


@csrf_exempt
def user_register(request):
    if request.method == "POST":
        body = json.loads(request.body.decode())
        account = body.get("account")
        pwd = body.get("pwd")
        result = Result()
        if len(User.objects.filter(account=account)) == 0:
            user = User(account=account, password=pwd, portrait_url="", is_admin=0, num_of_wiki=0)
            try:
                user.save()
                result.setOK()
                return HttpResponse(str(result))
            except:
                result.setStatusCode(-2)
                return HttpResponse(str(result))
        else:
            result.setStatusCode(-1)
            return HttpResponse(str(result))


@csrf_exempt
def user_login(request):
    if request.method == "POST":
        result = Result()
        body = json.loads(request.body.decode())
        account = body.get("account")
        pwd = body.get("pwd")
        query_res = User.objects.filter(account=account)
        if len(query_res) == 0:
            result.setData("data", "用户名不存在")
            return HttpResponse(str(result))
        else:
            user = query_res[0]
            if pwd != user.password:
                result.setData("data", "密码不正确")
                return HttpResponse(str(result))
            elif account == "admin":
                result.setStatuscode(1)
                return HttpResponse(str(result))
            else:
                result.setOK()
                return HttpResponse(str(result))


@csrf_exempt
def find_celebrity(request):
    if request.method == "GET":
        result = Result()
        query_res = User.objects.order_by(F("num_of_wiki").desc()).exclude(account="admin")
        if len(query_res) > 3:
            data = [{"account": user.account, "portrait_url": user.portrait_url, "num_of_wiki": user.num_of_wiki} for
                    user in query_res[0:3]]
        else:
            data = [{"account": user.account, "portrait_url": user.portrait_url, "num_of_wiki": user.num_of_wiki}
                    for user in query_res]
        result.setOK()
        result.setData("data", data)
        return HttpResponse(str(result))


@csrf_exempt
def user_portrait(request):
    result = Result()
    if request.method == "POST":
        body = json.loads(request.body.decode())
        account = body.get("account")
        portrait_url = body.get("portrait_url")
        query_res = User.objects.filter(account=account)
        if len(query_res) == 0:
            return HttpResponse(str(result))
        else:
            user = query_res[0]
            print(portrait_url)
            user.portrait_url = portrait_url
            user.save(update_fields=["portrait_url"])
            result.setOK()
            return HttpResponse(str(result))
    if request.method == "GET":
        account = request.GET.get("account")
        query_res = User.objects.filter(account=account).get()
        result.setOK()
        result.setData("portrait_url", query_res.portrait_url)
        return HttpResponse(str(result))


@csrf_exempt
def view_profile(request):
    if request.method == "GET":
        result = Result()
        account = request.GET.get("account")
        query_res = User.objects.filter(account=account)
        if len(query_res) == 0:
            return HttpResponse(str(result))
        else:
            # TODO 连接查询
            #data=[{"wiki_id":w.,"t"} for w in User.objects.filter(WikiUser__Wiki__user_account=account,wikiuser__relationship=1).all()]
            # data = [{"wiki_id": w.wiki_id, "title": w.wiki.title, "status": w.wiki.status} for w in
            #         WikiUser.objects.filter(Wiki__User_account=account, relationship=1).all()]
            # result.setData("1", data)
            # data = [{"wiki_id": w.wiki_id, "title": w.wiki.title, "status": w.wiki.status} for w in
            #         WikiUser.objects.filter(Wiki__User_account=account, relationship=2).all()]
            #result.setData("2", data)
            result.setOK()
            return HttpResponse(str(result))


@csrf_exempt
def update_wiki_status(request):
    if request.method == "POST":
        result = Result()
        body = json.loads(request.body.decode())
        wiki_id = body.get("wiki_id")
        status = body.get("status")
        query_res = Wiki.objects.filter(id=wiki_id)
        if len(query_res) == 0:
            result.setData("data", "wiki不存在")
            return HttpResponse(str(result))
        else:
            w = query_res[0]
            w.status = status
            w.save(update_fields=["status"])
            result.setOK()
            return HttpResponse(str(result))


@csrf_exempt
def review_wiki(request):
    if request.method == "GET":
        result = Result()
        query_res = Wiki.objects.filter(status=0)
        data = [{"title": w.title, "wiki_id": w.id} for w in query_res]
        result.setOK()
        result.setData("data", data)
        return HttpResponse(str(result))
