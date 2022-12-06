from django.db.models import Count

from animal.models import *

menu = [
    {'title': "О нас", 'url_name': 'about'},
    {'title': "Обратная связь", 'url_name': 'feedback'},
    {'title': "Добавить анкету", 'url_name': 'addpage'},
]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        categories = Category.objects.annotate(Count('animal'))
        context['menu'] = menu
        context['categories'] = categories
        return context
