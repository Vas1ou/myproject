from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Категория не выбрана'

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 20:
            raise ValidationError('Превышен лимит в 20 символов')
        return title

    class Meta:
        model = Animal
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'category']

