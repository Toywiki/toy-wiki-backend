# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 03:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('account', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('password', models.CharField(blank=True, max_length=250, null=True)),
                ('portrait_url', models.CharField(blank=True, max_length=45, null=True)),
                ('last_login', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_admin', models.IntegerField(blank=True, null=True)),
                ('num_of_wiki', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
                'swappable': 'AUTH_USER_MODEL',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField(blank=True, null=True)),
                ('time', models.DateTimeField(auto_now=True, null=True)),
                ('wiki_title', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'comment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Wiki',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=45, null=True)),
                ('introduction', models.TextField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Accept'), (-1, 'Deny'), (0, 'Censoring')], default=0)),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
                ('img_url', models.CharField(blank=True, max_length=45, null=True)),
                ('category', models.CharField(blank=True, max_length=45, null=True)),
                ('hits', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'db_table': 'wiki',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WikiUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relationship', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'wiki_user',
                'managed': False,
            },
        ),
    ]
