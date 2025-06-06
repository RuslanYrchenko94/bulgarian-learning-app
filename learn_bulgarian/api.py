from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Word, FlashCard
from .serializers import WordSerializer, FlashCardSerializer


class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer


class FlashCardViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = FlashCardSerializer

    def get_queryset(self):
        return FlashCard.objects.filter(user=self.request.user)