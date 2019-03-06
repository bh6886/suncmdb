# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from blog.models import *
admin.site.register(Employee)
admin.site.register(IPAAA)
admin.site.register(IP)