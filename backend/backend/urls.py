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
from toywiki.views import Upload_img, Create_wiki, View_wiki, Save_wiki, Edit_wiki, \
    Wiki_Comment, View_comment, Search_wiki_category, Search_wiki_title, Hot_wiki

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^uploadimage', Upload_img.as_view()),
                  url(r'^wiki/createwiki', Create_wiki.as_view()),
                  url(r'^wiki/viewwiki', View_wiki.as_view()),
                  url(r'^wiki/createwiki', Create_wiki.as_view),
                  url(r'^wiki/editwiki', Edit_wiki.as_view()),
                  url(r'^wiki/savewiki', Save_wiki.as_view()),
                  url(r'^wiki/comment', Wiki_Comment.as_view()),
                  url(r'^wiki/viewcomment', View_comment.as_view()),
                  url(r'^wiki/searchwiki_title', Search_wiki_title.as_view()),
                  url(r'^wiki/searchwiki_category', Search_wiki_category.as_view()),
                  url(r'^wiki/hotwiki', Hot_wiki.as_view()),

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
