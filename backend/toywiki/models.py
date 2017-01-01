from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    account = models.CharField(primary_key=True, max_length=45)
    password = models.CharField(max_length=250, blank=True, null=True)
    portrait_url = models.CharField(max_length=45, blank=True, null=True)
    is_admin = models.IntegerField(blank=True, null=True)
    num_of_wiki = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'User'


class Wiki(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(max_length=45, blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    img_url = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Wiki'


class WikiUser(models.Model):
    wiki = models.ForeignKey(Wiki, models.DO_NOTHING, db_column='Wiki_ID')  # Field name made lowercase.
    user_account = models.ForeignKey(User, models.DO_NOTHING, db_column='User_account')  # Field name made lowercase.
    relationship = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Wiki_User'
        unique_together = (('wiki', 'user_account'),)


class Comment(models.Model):
    comment_id = models.IntegerField(db_column='comment_ID')  # Field name made lowercase.
    content = models.TextField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    wiki = models.ForeignKey(Wiki, models.DO_NOTHING, db_column='Wiki_ID')  # Field name made lowercase.
    user_account = models.ForeignKey(User, models.DO_NOTHING, db_column='User_account')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comment'
        unique_together = (('comment_id', 'wiki', 'user_account'),)
