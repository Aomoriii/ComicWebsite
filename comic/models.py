"""
@Time    : 2021/8/29 15:04
@Author  : Aomori
@File    : models.py
"""
from django.db import models
from django.urls import reverse
# Create your models here.


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    type_name = models.CharField(max_length=255)

    def __str__(self):
        return self.type_name

    class Meta:
        managed = False
        db_table = 'Category'

    def get_absolute_url(self):
        return reverse('comic:category_list', kwargs={'pk': self.id})


class Comic(models.Model):
    comic_id = models.IntegerField(primary_key=True)
    comic_name = models.CharField(max_length=255)
    category = models.ForeignKey('Category',models.DO_NOTHING)
    author = models.CharField(max_length=255)
    context = models.CharField(max_length=255)
    pictures = models.CharField(max_length=10000)

    class Meta:
        managed = False
        db_table = 'Comic'

    def get_absolute_url(self):
        return reverse('comic:comic_chapter_list', kwargs={'comic_pk': self.comic_id})


class Charter(models.Model):
    charter_id = models.IntegerField(primary_key=True)
    charter_name = models.CharField(max_length=255)
    comic_id = models.ForeignKey('Comic', models.DO_NOTHING)
    src = models.CharField(max_length=10000)

    class Meta:
        managed = False
        db_table = 'Charter'

    def get_absolute_url(self):
        return reverse('comic:chapter_src', kwargs={'charter_pk': self.charter_id})
