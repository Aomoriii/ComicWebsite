#*-* coding=utf-8 -*-
"""
@Time    : 2021/8/29 15:04
@Author  : Aomori
@File    : admin.py
"""
from django.contrib import admin

from .models import Comic, Category, Charter

admin.site.site_header = '后台'  # 设置header
admin.site.site_title = '管理后台'   # 设置title
admin.site.index_title = '管理'

class ComicAdmin(admin.ModelAdmin):
    list_display = ['comic_id', 'comic_name', 'category', 'author', 'context', 'pictures']
    fields = ['comic_id', 'comic_name', 'category', 'author', 'context', 'pictures']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_name']

class CharterAdmin(admin.ModelAdmin):
    list_display = ['charter_id', 'charter_name', 'comic_id']
admin.site.register(Comic, ComicAdmin)
admin.site.register(Charter, CharterAdmin)
admin.site.register(Category, CategoryAdmin)


