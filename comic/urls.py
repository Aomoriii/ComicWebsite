# -*- coding: utf-8 -*-
"""
@Time    : 2021/8/29 15:04
@Author  : Aomori
@File    : urls.py
"""

from django.urls import path
from comic import views

app_name = 'comic'
urlpatterns = [
    path('',views.Index,name='index'),
    path('comic/<int:comic_pk>',views.comic_chapter,name='comic_chapter_list'),
    path('chapter/<int:charter_pk>',views.chapter_src,name='chapter_src'),
    path('search/',views.search,name='search'),
    path('category/<int:pk>',views.category,name='category_list'),
]