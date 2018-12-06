# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
class IP(models.Model):
    db = models.CharField(max_length=30)
    yy = models.CharField(max_length=30)
    class Meta:
        verbose_name='应用Ip'
        verbose_name_plural='记录应用数据库与Ip地址'
    def __unicode__(self):
        return u'数据库IP :%s     应用ip: %s' % (self.db, self.yy)

class DEP(models.Model):
    yyname = models.CharField(max_length=20)
    logdir = models.CharField(max_length=80)
    class Meta:
        verbose_name='路径信息'
        verbose_name_plural='记录应用名字日志路径等'
    def __unicode__(self):
        return u'应用名:%s   日志完整路径%s' % (self.yyname, self.logdir)