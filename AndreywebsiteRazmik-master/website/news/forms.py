from .models import Artiles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArtilesForm(ModelForm):
    class Meta:
        model = Artiles
        fields = ['title', 'anons', 'full_text', 'date', 'name', 'second_name', 'primary_key']


        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            'second_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            'primary_key': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ключ'
            }),


        }