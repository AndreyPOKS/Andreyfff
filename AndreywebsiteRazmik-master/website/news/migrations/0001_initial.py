# Generated by Django 4.1.7 on 2023-03-27 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('anons', models.CharField(max_length=250, verbose_name='Анонс')),
                ('name', models.CharField(max_length=250, verbose_name='Имя')),
                ('second_name', models.CharField(max_length=250, verbose_name='Фамилия')),
                ('primary_key', models.CharField(max_length=250, verbose_name='Ключ')),
                ('full_text', models.TextField(verbose_name='Статья')),
                ('date', models.DateTimeField(verbose_name='Дата публикации')),

            ],
        ),
    ]