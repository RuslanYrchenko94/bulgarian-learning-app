from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .api import WordViewSet, FlashCardViewSet

app_name = 'learn_bulgarian'
router = DefaultRouter()
router.register(r'api/words', WordViewSet)
router.register(r'api/flashcards', FlashCardViewSet)
urlpatterns = [
    path('', views.home, name='home'),
    path('dictionary/', views.dictionary, name='dictionary'),
    path('lessons/', views.lessons_list, name='lessons_list'),
] + router.urls