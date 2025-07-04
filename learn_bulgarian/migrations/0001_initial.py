# Generated by Django 5.2.2 on 2025-06-06 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Назва уроку')),
                ('content', models.TextField(verbose_name='Зміст уроку')),
                ('level', models.IntegerField(default=1, verbose_name='Рівень складності')),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bulgarian', models.CharField(max_length=100, verbose_name='Болгарське слово')),
                ('translation', models.CharField(max_length=100, verbose_name='Переклад')),
                ('example', models.TextField(blank=True, verbose_name='Приклад використання')),
                ('category', models.CharField(blank=True, max_length=50, verbose_name='Категорія')),
            ],
        ),
    ]
