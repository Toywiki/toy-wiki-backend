from django.db import models


class User(models.Model):
    account = models.CharField(primary_key=True, max_length=45)
    password = models.CharField(max_length=250, blank=True, null=True)
    portrait_url = models.CharField(max_length=45, blank=True, null=True)
    is_admin = models.IntegerField(blank=True, null=True)
    num_of_wiki = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class Wiki(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    img_url = models.CharField(max_length=45, blank=True, null=True)
    category = models.CharField(max_length=45, blank=True, null=True)
    hits = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wiki'

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    content = models.TextField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    wiki = models.ForeignKey('Wiki', models.DO_NOTHING, blank=True, null=True)
    user_account = models.ForeignKey('User', models.DO_NOTHING, db_column='user_account', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'



class WikiUser(models.Model):
    wiki = models.ForeignKey(Wiki, models.DO_NOTHING)
    user_account = models.ForeignKey(User, models.DO_NOTHING, db_column='user_account')
    relationship = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wiki_user'
        unique_together = (('wiki', 'user_account'),)
