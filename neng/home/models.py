# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible





class user_info(models.Model):
    name=models.CharField(max_length=256)
    password=models.CharField(max_length=256)
    status=models.IntegerField()
    create_time=models.DateTimeField(auto_now=True)
    modefi_time=models.DateTimeField(auto_now_add=True)
class article(models.Model):
    title=models.CharField("标题",max_length=256)
    content = models.TextField('内容', default='', blank=True)
    uid=models.IntegerField()
    status=models.IntegerField()
    create_time=models.DateTimeField(auto_now=True)
    modefi_time=models.DateTimeField(auto_now_add=True)
class article_discuss(models.Model):
    content = models.TextField('内容', default='', blank=True)
    uid=models.IntegerField()
    status=models.IntegerField()
    create_time=models.DateTimeField(auto_now=True)
    modefi_time=models.DateTimeField(auto_now_add=True)