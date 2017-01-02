from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)


class UserManager(BaseUserManager):
    def _create_user(self, account, password,
                     is_superuser, **extra_fields):
        user = self.model(account=account, is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, account, password=None, **extra_fields):
        return self._create_user(account, password, False, **extra_fields)

    def create_superuser(self, account, password, **extra_fields):
        return self._create_user(account, password, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    account = models.CharField(primary_key=True, max_length=45)
    password = models.CharField(max_length=250, blank=True, null=True)
    portrait_url = models.CharField(max_length=45, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    is_superuser = models.IntegerField(blank=True, null=True)
    num_of_wiki = models.IntegerField(blank=True, null=True)

    objects = UserManager()
    USERNAME_FIELD = 'account'
    REQUIRED_FIELDS = []

    class Meta:
        managed = False
        db_table = 'user'
        swappable = 'AUTH_USER_MODEL'

    def get_full_name(self):
        return self.account

    def get_short_name(self):
        return self.account


class Wiki(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    # 审核不通过：-1； 正在审核：0,； 审核通过：1；
    status = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    img_url = models.CharField(max_length=45, blank=True, null=True)
    category = models.CharField(max_length=45, blank=True, null=True)
    hits = models.IntegerField(blank=True, null=True, default=0)

    class Meta:
        managed = False
        db_table = 'wiki'


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    content = models.TextField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True, auto_now=True)
    wiki_title = models.CharField(max_length=45, blank=True, null=True)
    user_account = models.ForeignKey('User', models.DO_NOTHING, db_column='user_account', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'


class WikiUser(models.Model):
    wiki = models.ForeignKey(Wiki, models.DO_NOTHING)
    user_account = models.ForeignKey(User, models.DO_NOTHING, db_column='user_account')
    # 创建：1； 修改：2
    relationship = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wiki_user'
        unique_together = (('wiki', 'user_account'),)
