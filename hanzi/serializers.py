from rest_framework import serializers
from hanzi.models import ChineseCharacters


class ChineseCharactersSerializer(serializers.ModelSerializer):
	class Meta:
		model = ChineseCharacters
		fields = ('id', 'simplified', 'traditional', 'allusion', 'pinyin', 'img_file')
		

class ListSerializer(serializers.ModelSerializer):
	class Meta:
		model = ChineseCharacters
		fields = ('id', 'simplified', 'traditional', 'allusion')
