#coding:utf-8
import re
from django.shortcuts import render
from home import  models
from django import forms
import math
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator
from django.http import JsonResponse
import json
#表单
class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())

def test(request,page='1'):
    cc=1
    if request.session.get("uid"):
        cc=2
    pagenum=10
    # page=int(request.Get.get('page'))
    # page=request.get('page',"")
    num=int(page)
    startpage=(num-1)*pagenum
    endpage=num*pagenum
    hh= models.article.objects.all()[startpage:endpage]
    allpage=models.article.objects.count()
    gg=math.ceil(allpage/pagenum)
    return render(request,'test.html',{'uf':hh,'allpage':range(1,gg+1),"ww":cc})

def index1(request):

     return render(request,'wan.html',)
def wan(request):
    a=request.POST.get('con')
    print (a)
    return JsonResponse({"a":a})

def index(request):
    shu=models.my.objects.all()
    aa=[]
    for i in shu:
        title=i.title
        content=i.content
        co={'title':title,'content':content}
        aa.append(co)
    bb={'content':aa,'code':1}

    return JsonResponse(bb)
def admin(request):
    cc=1
    return render(request,'admin.html',{"ww":cc})

def tijiao(request):
    con=request.POST.get("con")
    title=request.POST.get("title")
    uid=request.session.get("id")
    add=models.article(title=title,content=con,status=1,uid=uid)
    add.save()
    return JsonResponse({"code":1,"message":"发布成功"})

def up(requset):
    f=requset.FILES.get('imgFile', None)
    with open("d://1.png","wb") as ff:
        ff.write(f.read())
        dict_tmp = {}
        dict_tmp["error"] = 0
        dict_tmp["url"] = "/static/1.png"
    return HttpResponse(json.dumps(dict_tmp))
def login(request):
    cc=1
    if request.session.get("uid"):
        cc=2
    return render(request,'login.html',{"ww":cc})
def mobilelogin(request):
    user=request.POST.get("user")
    ps=request.POST.get("pass")

    if models.user_info.objects.filter(name=user):
        if models.user_info.objects.filter(name=user,password=ps):
            id=models.user_info.objects.values("id").filter(name=user)
            print (id)
            request.session["uid"]=user
            request.session["id"]=id[0]['id']
            return  JsonResponse({"code":1,"message":"登录成功"})
        else:
            return  JsonResponse({"code":-2,"message":"密码错误"})
    else:
        return  JsonResponse({"code":-1,"message":"用户不存在"})
#注册
def register(request):
    cc=1
    if request.session.get("uid"):
        cc=2
    return render(request,'register.html',{"ww":cc})
def mobileregister(request):
    user=request.POST.get("user")
    ps=request.POST.get("pass")
    if models.user_info.objects.filter(name=user):
        return JsonResponse({"code":-1,"message":"已存在该用户名"})
    else:
        add=models.user_info(name=user,password=ps,status=1)
        add.save()
        # id=models.user_info.objects.values("id").filter(name=user)
        request.session["uid"]=user
        request.session["id"]=add.id
        print(add.id)
        return JsonResponse({"code":1,"message":"注册成功"})
def loginout(request):
    print ("退出")
    del  request.session["uid"]
    del  request.session["id"]
    cc=1
    return JsonResponse({"code":1,"message":"成功退出","ww":cc})

def search(request):
    print (request.POST.get("search"))
    return HttpResponse("真棒")