from django.db import models


# Create your models here.
class ChineseCharacters(models.Model):
	id = models.IntegerField(primary_key=True)  # 简体
	simplified = models.CharField(max_length=10, blank=True, default='', verbose_name='简体中文') # 简体
	traditional = models.CharField(max_length=10, blank=True, default='', verbose_name='繁体中文') # 繁体
	created = models.DateTimeField(auto_now_add=True)
	allusion = models.TextField(blank=True, default='', verbose_name='文字典故')  # 典故
	pinyin = models.CharField(max_length=20, blank=True, default='', verbose_name='拼音')  # 拼音
	img_file = models.FileField(default='', upload_to='', storage=None, verbose_name='存储位置')
