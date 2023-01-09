from django.db.models import Count

from .models import *

menu = [
    {'title': "О нас", 'url_name': 'about'},
    {'title': "Обратная связь", 'url_name': 'feedback'},
    {'title': "Добавить анкету", 'url_name': 'addpage'},
]


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(2)
        context = kwargs
        categories = Category.objects.annotate(Count('animal'))
        context['menu'] = user_menu
        context['categories'] = categories
        return context
