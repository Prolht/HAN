from rest_framework import serializers
from hanzi.models import ChineseCharacters, Poem


class ChineseCharactersSerializer(serializers.ModelSerializer):
	class Meta:
		model = ChineseCharacters
		fields = ('id', 'simplified', 'traditional', 'allusion', 'pinyin', 'img_file')
		

class ListSerializer(serializers.ModelSerializer):
	class Meta:
		model = ChineseCharacters
		fields = ('id', 'simplified', 'traditional', 'allusion')


class PoemSerializer(serializers.ModelSerializer):
	class Meta:
		model = Poem
		fields = ('author', 'title', 'content', 'dynasty')
