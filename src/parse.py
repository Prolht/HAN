import codecs
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with codecs.open(BASE_DIR+'\\hanzi.txt', encoding='utf-8') as f:
	hanzi = f.read()
hanzi_list = list(hanzi)
with codecs.open(BASE_DIR+'\\hanzi_list.txt', encoding='utf-8', mode='a+') as f:
	for hanzi in hanzi_list:
		f.write(hanzi + '\n')

