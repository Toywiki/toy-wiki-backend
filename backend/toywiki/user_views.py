from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.http import HttpRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import json
from toywiki.models import User, Wiki, WikiUser
from toywiki.utils import Result
from django.db.models import F


class Register(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Register, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        body = json.loads(request.body.decode())
        account = body.get("account")
        pwd = body.get("pwd")
        result = Result()
        default_partrait = "/media/default.png"
        if len(User.objects.filter(account=account)) == 0:
            user = User.objects.create_user(account=account, password=pwd, portrait_url=default_partrait, num_of_wiki=0)
            user.save()
            result.setOK()
        else:
            result.setStatusCode(-1)
        return HttpResponse(json.dumps(result))


class Login(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Login, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        result = Result()
        body = json.loads(request.body.decode())
        account = body.get("account")
        pwd = body.get("pwd")
        query_res = User.objects.filter(account=account)
        if len(query_res) == 0:
            result.setData("data", "用户名不存在")
            return HttpResponse(json.dumps(result))
        user = authenticate(account=account, password=pwd)
        if user is not None:
            result.setOK()
            login(request, user)
        else:
            result.setData("data", "密码不正确")
        return HttpResponse(json.dumps(result), content_type='application/json')


class Logout(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Logout, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        result = Result()
        logout(request)
        result.setOK()
        return HttpResponse(json.dumps(result))


class Password(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Password, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        result = Result()
        body = json.loads(request.body.decode())
        account = body.get("account")
        old_pwd = body.get("old_pwd")
        new_pwd = body.get("new_pwd")
        query_res = User.objects.filter(account=account)
        if len(query_res) == 0:
            result.setData("data", "用户名不存在")
            return HttpResponse(json.dumps(result))
        user = authenticate(account=account, password=old_pwd)
        if user is not None:
            user.set_password(new_pwd)
            user.save()
            result.setOK()
            return HttpResponse(json.dumps(result))
        else:
            result.setData("data", "密码不正确")
            return HttpResponse(json.dumps(result))



class Celebrity(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Celebrity, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        result = Result()
        query_res = User.objects.order_by(F("num_of_wiki").desc()).exclude(is_admin=1)
        if len(query_res) > 3:
            data = [{"account": user.account, "portrait_url": user.portrait_url, "num_of_wiki": user.num_of_wiki} for
                    user in query_res[0:3]]
        else:
            data = [{"account": user.account, "portrait_url": user.portrait_url, "num_of_wiki": user.num_of_wiki}
                    for user in query_res]
        result.setOK()
        result.setData("data", data)
        return HttpResponse(json.dumps(result))


class Portrait(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Portrait, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        result = Result()
        body = json.loads(request.body.decode())
        account = body.get("account")
        portrait_url = body.get("portrait_url")
        query_res = User.objects.filter(account=account)
        if len(query_res) == 0:
            return HttpResponse(json.dumps(result))
        else:
            user = query_res[0]
            print(portrait_url)
            user.portrait_url = portrait_url
            user.save(update_fields=["portrait_url"])
            result.setOK()
            return HttpResponse(json.dumps(result))

    def get(self, request):
        result = Result()
        account = request.GET.get("account")
        query_res = User.objects.filter(account=account).get()
        result.setOK()
        result.setData("portrait_url", query_res.portrait_url)
        return HttpResponse(json.dumps(result))


class Profile(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Profile, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        result = Result()
        account = request.GET.get("account")
        data = [{"wiki_id": w.id, "title": w.title, "status": w.status} for w in
                Wiki.objects.filter(wikiuser__user_account=account, wikiuser__relationship=1).select_related()]
        result.setData("create", data)
        data = [{"wiki_id": w.id, "title": w.title, "status": w.status} for w in
                Wiki.objects.filter(wikiuser__user_account=account, wikiuser__relationship=2).select_related()]
        result.setData("modified", data)
        result.setOK()
        return HttpResponse(json.dumps(result))
