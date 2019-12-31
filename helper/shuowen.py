# -*-  coding:utf-8 -*-
#爬动态网站
__author__ ='LUO'

import os
import random
import time
import codecs

from bs4 import BeautifulSoup
from urllib import request
import requests



global headers
headers = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
			'Accept': 'application/json, text/javascript, */*; q=0.01',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'zh-CN,zh;q=0.9',
			'Connection': 'keep-alive'
}


def get_img_url(url):
	response = requests.get(url, headers=headers)
	response.encoding = response.apparent_encoding
	# print(response.text)
	soup = BeautifulSoup(response.text, 'html.parser')
	img_ = soup.find_all('img')  # 找到所有含img的标签
	word = soup.find_all('input')[0].get('value')

	for each in img_:
		src = str(each.get('src'))
		if src.endswith('f'):
			return src, word
	return '', word


def download_img(url,filename):
	global headers
	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	try:
		os.mkdir(BASE_DIR + '\\' + word)
	except Exception as e:
		print(e)
	if url:
		filename = BASE_DIR + '\\' + word + '\\' + 'hanzi.jpg'
		try:
			req = request.Request(url=url, headers=headers)
			print('下载图片%s中' % word)
			binary_data = request.urlopen(req).read() #获取图片的二进制数据
			temp_file = open(filename, 'wb') #创建文档
			temp_file.write(binary_data)#将二进制文件写入文档中
			temp_file.close() #关闭文档
			#这种下载方法总是被禁 request.urlretrieve(imgurl, path + '%s.jpg' % n)  # 下载图片，并以path+数字的格式进行命名
			print('下载图片%s完毕' % filename)
		except Exception as e:
			print(e)
	else:
		pass


def main():
	BASE_URL = 'http://shuowen.chaziwang.com/shuowen-%s.html'
	n = 6894
	while n <= 7000:
		slp = random.randint(0, 3)
		n = n + 1
		url = BASE_URL % str(n)
		url, word = get_img_url(url)
		download_img(url, word)
		time.sleep(slp)
		

def main2():
	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	dirlist = []
	for dirs in os.listdir(BASE_DIR):
		if os.path.isdir(dirs):
			dirlist.append(dirs)
	for dirli in dirlist:
		try:
			os.rename(dirli+'\\hanzi.jpg', dirli + ".jpg")
		except Exception as e:
			pass



if __name__ == '__main__':
	main2()
