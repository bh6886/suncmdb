"""untitled2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from blog.views  import *
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^index1', TemplateView.as_view(template_name="index_1.html")),
    url(r'^undefined', TemplateView.as_view(template_name="index_1.html")),
    url(r'^table', TemplateView.as_view(template_name="table.html")),
    url(r'^dep', TemplateView.as_view(template_name="dep.html")),
    url(r'^login/$', login),
    url(r'^loginout/$', loginout),
    url(r'^accounts/login/$', login),
    url(r'^get', get),



    # url(r'^get', get),
    # url(r'^table', TemplateView.as_view(template_name="table.html")),
]


