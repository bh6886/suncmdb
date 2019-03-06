# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
class IPAAA(models.Model):
    aaa = models.CharField(max_length=30)
    bbb = models.CharField(max_length=30)
    class Meta:
        verbose_name='应用Ip'
        verbose_name_plural='记录应用数据库与Ip地址'
    def __unicode__(self):
        return u'数据库IP :%s     应用ip: %s' % (self.aaa, self.bbb)

class Employee(models.Model):			#父类是Model
    name = models.CharField(max_length=20)	#创建一个字段name,类属性就会自动映射到数据库当中表的一个字段类型是CharField，最大长度是20
    def __unicode__(self):#当我们把对象以字符串方式反馈的时候，这时候把对应的name表现出来，说白了就是让人能看到自己数据库里的值，不然都是object
                return self.name
class IP(models.Model):
    db = models.CharField(max_length=30)
    yy = models.CharField(max_length=30)
    class Meta:
        verbose_name='服务器'
        verbose_name_plural='服务器列表'
    def __unicode__(self):
         return '%s, %s'% (self.yy, self.db)