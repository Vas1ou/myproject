from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import *

menu = [
    {'title': "О нас", 'url_name': 'about'},
    {'title': "Обратная связь", 'url_name': 'feedback'},
    {'title': "Добавить анкету", 'url_name': 'addpage'},
]


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_post(request, post_slug):
    user_menu = menu.copy()
    post = get_object_or_404(Animal, slug=post_slug)
    categories = Category.objects.all()
    return render(request, 'animal/post.html',
                  {'post': post, 'menu': user_menu, 'title': post.title, 'categories': categories})

#
# class AnimalHome(ListView):
#     model = Animal
#     template_name =
#




def index(request):
    user_menu = menu.copy()
    animals = Animal.objects.all()
    categories = Category.objects.all()
    return render(request, 'animal/index.html', {'animals': animals, 'menu': user_menu,
                                                 'categories': categories, 'title': 'Главная страница'})


def get_category(request, category_slug):
    user_menu = menu.copy()
    categories = Category.objects.all()
    animals = Animal.objects.filter(category__slug=category_slug)
    category = Category.objects.get(slug=category_slug)
    return render(request, 'animal/categories.html', {'menu': user_menu, 'categories': categories,
                                                      'animals': animals, 'title': category})


def about(request):
    return HttpResponse('О нас')


def feedback(request):
    return HttpResponse('Обратная связь')


def addpage(request):
    return HttpResponse('Добавить анкету')


def register(request):
    return HttpResponse('Регистрация')


def login(request):
    return HttpResponse('Войти')


def logout(request):
    return HttpResponse('Выйти')
