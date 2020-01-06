import sys
import os
import codecs
import json

import django
from pypinyin import pinyin as py
from django.db.models import Q

from src.zhtools import langconv


def simplified2traditional(simplified_word):
	# 简体到繁体转换
	line = langconv.Converter('zh-hant').convert(simplified_word)
	return line if line else ''

def get_pinyin(simplified_word):
	# 获取某个汉字的拼音
	_pinyin = py(simplified_word, heteronym=True)
	return ','.join(_pinyin[0]) if _pinyin else ''


BASE_DIR = os.path.dirname((os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Han.settings')
django.setup()


def dump_data(model, data):
	querysetlist = []
	all_file = insert_img()
	for i in range(len(data)):
		word = data[i].replace('\n', '')
		if word in all_file or simplified2traditional(word) in all_file:
			querysetlist.append(model(
				simplified=word,
				pinyin=get_pinyin(word),
				traditional=simplified2traditional(word),
				img_file='cha/' + word + '.jpg'
				))
		else:
			querysetlist.append(model(simplified=word, pinyin=get_pinyin(word), traditional=simplified2traditional(word)))
	model.objects.bulk_create(querysetlist)


def insert_img():
	path = 'E:\Coding\HAN\media\cha'
	all_files = os.listdir(path)
	all_file = [fi[0] for fi in all_files]
	return all_file


def import_songci(songci):
	querysetlist = []
	ci_base_dir = r'H:\Google\chinese-poetry-master\ci'
	ci_dirs = list()
	for ci_dir in os.listdir(ci_base_dir):
		if 'song' in ci_dir and 'ci' in ci_dir:
			ci_dir = ci_base_dir + '\\' + ci_dir
			with codecs.open(ci_dir, encoding='utf-8', mode='r') as ff:
				ci = json.load(ff)
				for f in ci:
					print(f)
					querysetlist.append(songci(
						author=f['author'],
						rhythmic=f['rhythmic'],
						content=''.join(f['paragraphs']),
					))
	songci.objects.bulk_create(querysetlist)


def import_songshi(shi):
	querysetlist = []
	ci_base_dir = r'H:\Google\chinese-poetry-master\json'
	ci_dirs = list()
	for ci_dir in os.listdir(ci_base_dir):
		if 'song' in ci_dir and 'poet' in ci_dir:
			ci_dir = ci_base_dir + '\\' + ci_dir
			try:
				with codecs.open(ci_dir, encoding='utf-8', mode='r') as ff:
					ci = json.load(ff)
					for f in ci:
						if len(f['title']) < 200 and len(f['title']) < 50:
							querysetlist.append(shi(
								author=f['author'],
								title=f['title'],
								content=''.join(f['paragraphs']),
								dynasty ='宋',
							))
			except Exception as e:
				print(e)
	shi.objects.bulk_create(querysetlist)


def import_tangshi(shi):
	querysetlist = []
	ci_base_dir = r'H:\Google\chinese-poetry-master\json'
	ci_dirs = list()
	for ci_dir in os.listdir(ci_base_dir):
		if 'tang' in ci_dir and 'poet' in ci_dir:
			ci_dir = ci_base_dir + '\\' + ci_dir
			try:
				with codecs.open(ci_dir, encoding='utf-8', mode='r') as ff:
					ci = json.load(ff)
					for f in ci:
						if len(f['title']) < 200 and len(f['title']) < 50:
							querysetlist.append(shi(
								author=f['author'],
								title=f['title'],
								content=''.join(f['paragraphs']),
								dynasty ='唐',
							))
			except Exception as e:
				print(e)
	shi.objects.bulk_create(querysetlist)

def import_shijing(shi):
	querysetlist = []
	ci_dir = r'H:\Google\chinese-poetry-master\shijing\shijing.json'
	try:
		with codecs.open(ci_dir, encoding='utf-8', mode='r') as ff:
			ci = json.load(ff)
			for f in ci:
				if len(f['title']) < 100 and len(f['title']) < 10:
					querysetlist.append(shi(
						section=f['section'],
						title=f['title'],
						content=''.join(f['content']),
						chapter =f['chapter'],
					))
	except Exception as e:
		print(e)
	shi.objects.bulk_create(querysetlist)


if __name__ == "__main__":
	from hanzi.models import ChineseCharacters
	# from hanzi.models import SongCi
	# from hanzi.models import Shi
	# from hanzi.models import ShiJing
	with codecs.open(BASE_DIR + '\\hanzi_list.txt', encoding='utf-8', mode='r') as f:
			data = f.readlines()
	dump_data(ChineseCharacters, list(set(data)))
	# import_songci(SongCi)
	# import_songshi(Shi)
	# import_tangshi(Shi)
	# import_shijing(ShiJing)