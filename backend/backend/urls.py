"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import auth_login, auth_logout
from django.conf.urls.static import static
from backend import settings
from toywiki.user_views import Register, Login, Logout, Password, Celebrity, Portrait, Profile
from toywiki.views import upload_img, create_wiki, view_wiki, save_wiki, edit_wiki, \
    comment, view_comment, search_wiki_category, search_wiki_title, hot_wiki

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^uploadimage', upload_img),
                  url(r'^wiki/createwiki', create_wiki),
                  url(r'^wiki/viewwiki', view_wiki),
                  url(r'^wiki/createwiki', create_wiki),
                  url(r'^wiki/editwiki', edit_wiki),
                  url(r'^wiki/savewiki', save_wiki),
                  url(r'^wiki/comment', comment),
                  url(r'^wiki/viewcomment', view_comment),
                  url(r'^wiki/searchwiki_title', search_wiki_title),
                  url(r'^wiki/searchwiki_category', search_wiki_category),
                  url(r'^wiki/hotwiki', hot_wiki),


                  url(r'^user/register', Register.as_view()),
                  url(r'^user/login', Login.as_view()),
                  url(r'^user/logout', Logout.as_view()),
                  url(r'^user/password', Password.as_view()),
                  url(r'^user/celebrity', Celebrity.as_view()),
                  url(r'^user/portrait', Portrait.as_view()),
                  url(r'^user/profile', Profile.as_view()),

              ] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
