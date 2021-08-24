#! usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2021/8/20 14:49
# @Author: wangjunjie
# @File: urls.py
# @Des:
from django.urls import path
from . import views

urlpatterns = [
    path('add', views.add_note),
    path('all_note', views.all_note),
    path('update_note/<int:note_id>', views.update_note),
    path('delete_note', views.delete_note),

]
