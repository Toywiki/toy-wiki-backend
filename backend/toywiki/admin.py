from django.contrib import admin
from toywiki.models import User, Wiki
from django.conf.urls import url
from functools import update_wrapper

# Register your models here.


admin.site.disable_action('delete_selected')


class WikiAdmin(admin.ModelAdmin):
    actions = None
    list_display = ['id', 'title','status']
    readonly_fields = ('id', 'title', 'introduction', 'content', 'img_url', 'category', 'hits','status')

    def get_queryset(self, request):
        qs = super(WikiAdmin, self).get_queryset(request)
        return qs.filter(status=1)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Wiki, WikiAdmin)


class MyWiki(Wiki):
    class Meta:
        proxy = True


class WikiStatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'status']
    ordering = ['title']
    actions = ['accept_wiki', 'deny_wiki']
    readonly_fields = ('id', 'title', 'introduction', 'content', 'img_url', 'category', 'hits')

    def accept_wiki(self, request, queryset):
        rows_updated = queryset.update(status=1)
        message = "成功将%s条wiki状态设置为通过" % rows_updated
        self.message_user(request, message)

    accept_wiki.short_description = "将选中的wiki状态设为通过"

    def deny_wiki(self, request, queryset):
        rows_updated = queryset.update(status=-1)
        message = "成功将%s条wiki状态设置为拒绝" % rows_updated
        self.message_user(request, message)

    deny_wiki.short_description = "将选中的wiki状态设为拒绝"

    def get_queryset(self, request):
        qs = super(WikiStatusAdmin, self).get_queryset(request)
        return qs.filter(status=0)

    def has_add_permission(self, request):
        return False


admin.site.register(MyWiki, WikiStatusAdmin)
