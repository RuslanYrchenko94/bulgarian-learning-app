from rest_framework import serializers
from .models import Word, FlashCard

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['id', 'bulgarian', 'translation', 'example', 'category']

class FlashCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashCard
        fields = ['id', 'user', 'word', 'next_review', 'repetition', 'ease_factor']