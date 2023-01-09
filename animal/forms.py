from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField

from .models import *


class AddPostForm(forms.ModelForm):
    captcha = CaptchaField(label='Напишите ответ')

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


# class RegisterUserForm(UserCreationForm):
#     first_name = forms.CharField(label='Имя пользователя', widget=forms.TextInput)
#     username = forms.CharField(label='Логин', widget=forms.TextInput)
#     email = forms.EmailField(label='Email', widget=forms.EmailInput)
#     password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput)
#     captcha = CaptchaField(label='Напишите ответ')
#
#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'email', 'password1', 'password2',)
#
#
# class LoginUserForm(AuthenticationForm):
#     username = forms.CharField(label='Логин', widget=forms.TextInput)
#     password = forms.CharField(label='Пароль', widget=forms.PasswordInput)


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=150, widget=forms.TextInput)
    email = forms.EmailField(label='Email', widget=forms.EmailInput)
    content = forms.CharField(label='Текст', widget=forms.Textarea)
    captcha = CaptchaField(label='Напишите ответ')
