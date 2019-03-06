# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.core import serializers
from blog.models import *

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from django.contrib.sessions.backends.db import SessionStore
from django.contrib.sessions.models import Session


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse('用户没有启用!')
        else:
            return HttpResponse('用户名或者密码错误！')
    else:
        return render_to_response('login.html')


def loginout(request):
    auth_logout(request)
    return HttpResponseRedirect('/login/')

@login_required
def index(req):
    return render_to_response('index.html')


def get(req):
    modules_info = []
    data = {}
    province = serializers.serialize("json", IP.objects.all())
    data["data"] = json.loads(province)

    for i in data["data"]:
        yy = i['fields']['yy']
        db = i['fields']['db']
        modules_info.append([yy, db])
        resp = {"draw": 1, "recordsTotal": 2, "recordsFiltered": 2, "data": modules_info}  # 拼接
    return HttpResponse(json.dumps(resp), content_type="application/json")



#
# def index(req):
#     ss = '123'
#     return render_to_response('index.html', {'ss': ss})



