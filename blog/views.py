# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from blog.models import *
from django.shortcuts import render_to_response
import pymysql

def select(sql):
    conn = pymysql.connect(user='root', passwd='123456', host='172.16.3.98', charset='utf8')
    cur = conn.cursor()
    conn.select_db('un2')
    cur.execute(sql)
    conn.commit()
    aa = cur.fetchone()
    cur.close()
    conn.close()
    return aa

def index(req):
    DB = IP.objects.all()[0].db
    YY = IP.objects.all()[0].yy
#     ss = r"docker run -d --restart=always --name drgs \
# --net huoshu --ip 172.21.1.5 -p 9998:9998 \
# -e ORACLE_ADDR=%s:1521:orcl \
# -e LANG='en_US.UTF-8' \
# -e HDC_ADDR=%s \
# -v /var/log/drgs:/opt/drgs/log " % (DB,YY)
#     sql= 'select yy from blokg_ip'
    sql = "select logdir from blog_dep where yyname='drgs'"
    ss = select(sql)[0]
    return render_to_response('index.html', {'ss': ss})



