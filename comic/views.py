#-*- coding=utf-8 -*-
"""
@Time    : 2021/8/29 15:04
@Author  : Aomori
@File    : views.py
"""

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from comic import models
from .models import Comic,Category,Charter
from django.views.generic import ListView,DetailView
from pure_pagination.mixins import PaginationMixin
from django.http import HttpResponse
from django.shortcuts import render


def search(requset):
    q = requset.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = '请输入关键词'
        return render(requset, 'comic/errors.html', {'error_msg': error_msg})

    comic_list = Comic.objects.filter(comic_name__icontains=q)
    return render(requset, 'comic/results.html', {'error_msg': error_msg, 'comic_list': comic_list})


def Index(request):
    recent_comics = Comic.objects.all()[:12]
    rank_comics = Comic.objects.all()[20:26]
    categorys = Category.objects.all()[:6]
    return render(request, 'comic/index.html', {'recent_comics': recent_comics, 'rank_comics': rank_comics,
                                                'categorys': categorys})


def comic_chapter(request, comic_pk):
    #获取该pk的漫画
    comic_details = Comic.objects.get(comic_id=comic_pk)
    #通过外键获取数据，charter是表名，表名为Charter，这里必须小写，加上后缀"_set"
    #意为：获取该漫画下的所有章节
    comic_chapters = comic_details.charter_set.all()
    return render(request,'comic/comic_chapter_list.html',context={'comic_details':comic_details,'comic_chapters':comic_chapters})


def chapter_src(request,charter_pk):
    #charter_pk 是主键，在数据库中是charter_id
    chapter_detials = Charter.objects.get(charter_id=charter_pk)
    temp_src = chapter_detials.src
    comic_srcs = temp_src.split(',')

    return render(request,'comic/chapter_src.html',context={'comic_srcs':comic_srcs})

def category(request,pk):
    categories = Category.objects.get(id=pk)
    category_comics = categories.comic_set.all()
    return render(request,'comic/category_list.html',context={'categories':categories,'category_comics':category_comics})

