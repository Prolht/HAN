from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from django.http import Http404
from django.db.models import Q

from hanzi.models import ChineseCharacters
from hanzi.serializers import ChineseCharactersSerializer
from Han.settings import get_logger

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


class CharactersView(APIView):
	def get_object(self, id):
		try:
			return ChineseCharacters.objects.get(id=id)
		except ChineseCharacters.DoesNotExist:
			logger.error('get_object wrong')
			raise Http404

	def get(self, request, id, format=None):
		characters = self.get_object(id)
		serializer = ChineseCharactersSerializer(characters)
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
		serializer = ChineseCharactersSerializer(characters, many=True)
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

