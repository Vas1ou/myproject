from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseNotFound, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import *

from .forms import *
from .utils import *


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class AnimalHome(DataMixin, ListView):
    model = Animal
    template_name = 'animal/index.html'
    context_object_name = 'animals'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        dm_context = self.get_user_context(title='Главная страница')
        return dict((list(context.items())) + list(dm_context.items()))

    def get_queryset(self):
        return Animal.objects.filter(is_published=True)


# def index(request):
#     animals = Animal.objects.all()
#     categories = Category.objects.all()
#     return render(request, 'animal/index.html', {'animals': animals, 'menu': menu,
#                                                  'categories': categories, 'title': 'Главная страница'})

class AnimalCategory(DataMixin, ListView):
    model = Animal
    template_name = 'animal/index.html'
    context_object_name = 'animals'
    allow_empty = False

    def get_queryset(self):
        return Animal.objects.filter(category__slug=self.kwargs['category_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        dm_context = self.get_user_context(title=str(context['animals'][0].category))
        return dict((list(context.items())) + list(dm_context.items()))


# def get_category(request, category_slug):
#     categories = Category.objects.all()
#     animals = Animal.objects.filter(category__slug=category_slug)
#     category = Category.objects.get(slug=category_slug)
#     return render(request, 'animal/categories.html', {'menu': menu, 'categories': categories,
#                                                       'animals': animals, 'title': category})

class ShowAnimal(DataMixin, DetailView):
    model = Animal
    template_name = 'animal/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        dm_context = self.get_user_context(title=context['post'])
        return dict((list(context.items())) + list(dm_context.items()))


# def show_post(request, post_slug):
#     post = get_object_or_404(Animal, slug=post_slug)
#     categories = Category.objects.all()
#     return render(request, 'animal/post.html',
#                   {'post': post, 'menu': menu, 'title': post.title, 'categories': categories})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'animal/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        dm_context = self.get_user_context(title=menu[2]['title'])
        return dict((list(context.items())) + list(dm_context.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'animal/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        dm_context = self.get_user_context(title='Регистрация')
        return dict((list(context.items())) + list(dm_context.items()))


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'animal/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        dm_context = self.get_user_context(title='Авторизация')
        return dict((list(context.items())) + list(dm_context.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)

    return redirect('login')


def about(request):
    categories = Category.objects.annotate(Count('animal'))
    return render(request, 'animal/about.html', {'title': 'О нас', 'categories': categories})


def feedback(request):
    return HttpResponse('Обратная связь')
