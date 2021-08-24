#! usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/8/19 13:58
# @Author: wangjunjie
# @File: urls.py
# @Des:
from django.urls import path
from . import views

urlpatterns = [
    path('reg', views.reg_view),
    path('login', views.login_view),
    path('logout', views.logout_view),
]
