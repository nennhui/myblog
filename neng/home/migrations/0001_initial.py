# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-18 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='标题')),
                ('content', models.TextField(blank=True, default='', verbose_name='内容')),
                ('uid', models.IntegerField()),
                ('status', models.IntegerField()),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('modefi_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='article_discuss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, default='', verbose_name='内容')),
                ('uid', models.IntegerField()),
                ('status', models.IntegerField()),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('modefi_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='user_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('password', models.CharField(max_length=256)),
                ('status', models.IntegerField()),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('modefi_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
