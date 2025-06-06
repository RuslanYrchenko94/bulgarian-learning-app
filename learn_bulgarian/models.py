from django.db import models
from django.contrib.auth.models import User


class Word(models.Model):
    bulgarian = models.CharField(max_length=100, verbose_name="Болгарське слово")
    translation = models.CharField(max_length=100, verbose_name="Переклад")
    example = models.TextField(blank=True, verbose_name="Приклад використання")
    category = models.CharField(max_length=50, blank=True, verbose_name="Категорія")

    def __str__(self):
        return f"{self.bulgarian} → {self.translation}"


class Lesson(models.Model):
    title = models.CharField(max_length=200, verbose_name="Назва уроку")
    content = models.TextField(verbose_name="Зміст уроку")
    level = models.IntegerField(default=1, verbose_name="Рівень складності")


    def __str__(self):
        return self.title


class FlashCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    next_review = models.DateField()
    repetition = models.IntegerField(default=0)
    ease_factor = models.FloatField(default=2.5)

    def __str__(self):
        return f"Картка {self.word.bulgarian} для {self.user.username}"

class Word(models.Model):
    # ... інші поля ...
    audio = models.FileField(upload_to='audio/', blank=True, null=True)


class UserProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    words_learned = models.ManyToManyField(Word)
    last_active = models.DateField(auto_now=True)

    def get_progress(self):
        total_words = Word.objects.count()
        learned = self.words_learned.count()
        return round((learned / total_words) * 100) if total_words else 0

