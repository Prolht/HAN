import datetime
import random

from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from django.http import Http404
from django.db.models import Q

from hanzi.models import ChineseCharacters, Poem
from hanzi.serializers import ChineseCharactersSerializer, ListSerializer, PoemSerializer
from Han.settings import get_logger
from helper.tools import convert2list

logger = get_logger()


class JSONResponse(HttpResponse):
	"""
    An HttpResponse that renders its content into JSON.
    """

	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)


class MyPageNumberPagination(PageNumberPagination):  # 分页
	# 每页显示多少个
    page_size = 10
	# 默认每页显示3个，可以通过传入pager1/?page=2&size=4,改变默认每页显示的个数、
    page_size_query_param = "size"
	# 最大页数不超过10000
    max_page_size = 10000
	# 获取页码数的
    page_query_param = "page"


class CharacterView(APIView):
	def get_object(self, character):
		try:
			return ChineseCharacters.objects.get(Q(simplified=character) | Q(traditional=character))
		except ChineseCharacters.DoesNotExist:
			logger.error('get_object wrong')
			raise Http404

	def post(self, request, format=None):
		character = request.data['character']
		print(character)
		character = self.get_object(character)
		serializer = ChineseCharactersSerializer(character)
		return Response(serializer.data)


class CharactersListView(APIView):
	def get_object(self):
		try:
			return ChineseCharacters.objects.all()
		except ChineseCharacters.DoesNotExist:
			logger.error('get_object wrong')
			raise Http404

	def get(self, request, format=None):
		characters = self.get_object()
		pg = MyPageNumberPagination()
		# 获取分页的数据
		pg_ = pg.paginate_queryset(queryset=characters, request=request, view=self)
		serializer = ListSerializer(pg_, many=True)
		return Response(serializer.data)


class CharactersSearchView(APIView):
	def get_object(self, character):
		try:
			return ChineseCharacters.objects.get(Q(simplified=character) | Q(traditional=character))
		except ChineseCharacters.DoesNotExist:
			logger.error('get_object wrong')
			raise Http404

	def post(self, request, format=None):
		character = request.data['character']
		character = self.get_object(character)
		serializer = ChineseCharactersSerializer(character)
		return Response(serializer.data)


class UpdateView(APIView):
	def post(self, request, format=None):
		try:
			simplified = request.data.get('simplified')
			traditional = request.data.get('traditional')
			allusion = request.data.get('allusion')
			pinyin = request.data.get('pinyin')
			item, created = ChineseCharacters.objects.get_or_create(simplified=simplified)
			item.traditional = traditional
			item.allusion = allusion
			item.pinyin = pinyin
			item.img_file = request.FILES.get('img')
			if item.size and item.size > 1 * 1024 * 1024:
				raise ValueError('图片大小不能超过1M')
			item.save()
			return Response({'mg': 'success', 'status': 200})
		except Exception as e:
			logger('update error ', e)
			raise Http404


from django.shortcuts import render
from hanzi.models import ChineseCharacters


def uploadImg(request):
	if request.method == 'POST':
		simplified = request.data.get('simplified')
		print(simplified)
		img = request.FILES.get('img')
		if img.size and img.size > 1 * 1024 * 1024:
			raise ValueError('图片大小不能超过1M')
		img, created = ChineseCharacters.objects.get_or_create(simplified='包')
		img.img_file = request.FILES.get('img')
	return render(request, 'uploading.html')


def showImg(request):
	imgs = ChineseCharacters.objects.get(simplified='包')
	content = {
		'imgs': imgs,
	}
	print(content)
	print(imgs.img_file)
	return render(request, 'showing.html', content)


class PoemView(APIView):
	def get_object(self, seed):
		poem_num = len(Poem.objects.all())
		# random_group_num = random.randrange(0, int(poem_num / seed))  # 组间随机
		# random_in_group_num = random.randrange(0, seed)  # 组内随机
		# random_id = random_group_num * seed + random_in_group_num
		random_id = seed % poem_num
		try:
			return Poem.objects.get(id=random_id)
		except Poem.DoesNotExist:
			logger.error('get_object wrong')
			raise Http404

	def get(self, request, format=None):
		dat = datetime.datetime.today()
		seed = int(str(dat.year) + str(dat.month) + str(dat.day))
		daily_poem = self.get_object(seed)
		daily_poem_serializer = PoemSerializer(daily_poem)
		content = convert2list(daily_poem_serializer.data['content'])
		res = {'title': daily_poem_serializer.data['title'], 'content': content}
		return Response(res)
		# return Response(daily_poem_serializer.data)
