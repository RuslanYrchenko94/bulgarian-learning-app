from django.urls import path
from .views import DictionaryView, LessonListView, LessonDetailView, home
from rest_framework.routers import DefaultRouter
from .api import WordViewSet, FlashCardViewSet

app_name = 'learn_bulgarian'
router = DefaultRouter()
router.register(r'api/words', WordViewSet)
router.register(r'api/flashcards', FlashCardViewSet)
urlpatterns = [
    path('', home, name='home'),
    path('dictionary/', DictionaryView.as_view(), name='dictionary'),
    path('lessons/', LessonListView.as_view(), name='lessons_list'),
    path('lesson/<int:pk>/', LessonDetailView.as_view(), name='lesson_detail'),
] + router.urls