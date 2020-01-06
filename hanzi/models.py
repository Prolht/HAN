import os
from django.db import models


# Create your models here.
class ChineseCharacters(models.Model):
	id = models.AutoField(primary_key=True)  # 简体
	simplified = models.CharField(max_length=10, blank=True, default='', verbose_name='简体中文', unique=True)  # 简体
	traditional = models.CharField(max_length=10, blank=True, default='', verbose_name='繁体中文') # 繁体
	created = models.DateTimeField(auto_now_add=True)
	allusion = models.TextField(blank=True, default='', verbose_name='文字典故')  # 典故
	pinyin = models.CharField(max_length=100, blank=True, default='', verbose_name='拼音')  # 拼音
	img_file = models.ImageField(default='', upload_to="cha/", blank=True, verbose_name='存储位置')


class SongCi(models.Model):
	id = models.AutoField(primary_key=True)
	author = models.CharField(max_length=10, blank=True, default='', verbose_name='作者')
	rhythmic = models.TextField(blank=True, default='', verbose_name='词牌名')
	content = models.TextField(blank=True, default='', verbose_name='词内容')
	dynasty = models.CharField(max_length=10, blank=True, default='宋', verbose_name='朝代')
	category = models.CharField(max_length=10, blank=True, default='词')


class Shi(models.Model):
	id = models.AutoField(primary_key=True)
	author = models.CharField(max_length=50, blank=True, default='', verbose_name='作者')
	title = models.CharField(max_length=200, blank=True, default='', verbose_name='诗名')
	content = models.TextField(blank=True, default='', verbose_name='诗内容')
	chapter = models.CharField(max_length=10, blank=True, default='', verbose_name='篇章')
	section = models.TextField(blank=True, default='', verbose_name='卷')
	dynasty = models.CharField(max_length=10, blank=True, default='', verbose_name='朝代')


class ShiJing(models.Model):
	id = models.AutoField(primary_key=True)
	chapter = models.CharField(max_length=10, blank=True, default='', verbose_name='作者')
	title = models.CharField(max_length=100, blank=True, default='', verbose_name='诗名')
	content = models.TextField(blank=True, default='', verbose_name='诗经内容')
	section = models.CharField(max_length=10, blank=True, default='', verbose_name='朝代')
