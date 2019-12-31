import sys
import os
import codecs

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

	# for i in all_file:
	# 	try:
	# 		img = model.objects.get(Q(simplified=i[0]) | Q(traditional=i[0]))
	# 		img.img_file = 'cha/' + i
	# 		img.save()
	# 	except Exception as e:
	# 		pass


if __name__ == "__main__":
	from hanzi.models import ChineseCharacters
	with codecs.open(BASE_DIR + '\\hanzi_list.txt', encoding='utf-8', mode='r') as f:
			data = f.readlines()
	dump_data(ChineseCharacters, list(set(data)))
	# get_pinyin('和')