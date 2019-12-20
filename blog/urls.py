#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2019/12/19 13:53
# @Author  : 三哥
# @Site    : 
# @File    : urls.py.py
# @Software: PyCharm
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
