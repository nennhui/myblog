"""neng URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from home import views
from django.conf import settings
from django.conf.urls import patterns, include, url
admin.autodiscover()
urlpatterns = [
    url(r'^test/page=([0-9]+)/$', views.test),
    url(r'^index/test/$', views.test),
    url(r'^index/$', views.index),
    url(r'^wan/$', views.wan),
    url(r'^admin/',views.admin),
     url(r'^index1/$', views.index1),
    url(r'^tijiao/$', views.tijiao),
    url(r'^up/$', views.up),
    url(r'^$', views.test),
    url(r'^index/login/$', views.login),
    url(r'^index/mobilelogin/$', views.mobilelogin),
    url(r'^index/register/$', views.register),
    url(r'^index/mobileregister/$', views.mobileregister),
    url(r'^index/loginout/$', views.loginout),
    url(r'^search/$', views.search),

]
