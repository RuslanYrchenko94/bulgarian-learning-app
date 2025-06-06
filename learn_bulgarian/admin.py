from django.contrib import admin
from .models import Word, Lesson

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('bulgarian', 'translation', 'category')
    search_fields = ('bulgarian', 'translation')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'level')
    search_fields = ('title', 'content')