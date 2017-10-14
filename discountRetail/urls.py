#encoding:utf-8

"""discountRetail URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from discountRetailApp import views as discountRetail_views

urlpatterns = [
    # url(r'^minus',discountRetail_views.minus,name='minus'),
    # # url(r'^add2/(\d+)/(\d+)/$',discountRetail_views.add2,name='add2'),
    # url(r'^add/(\d+)/(\d+)/$', discountRetail_views.add2, name='addfunc'),
    # url(r'^people', discountRetail_views.people, name='people'),
    # url(r'^base', discountRetail_views.base, name='base'),
    url(r'^$',discountRetail_views.index),
    url(r'^adduser$',discountRetail_views.adduser,name='adduser'),
    url(r'^uploadImg$',discountRetail_views.uploadImg,name='uploadImg'),

]
