# Generated by Django 4.1.7 on 2023-03-31 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artiles',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='artiles',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='artiles',
            name='second_name',
            field=models.CharField(max_length=50, verbose_name='Фамилия'),
        ),
    ]
