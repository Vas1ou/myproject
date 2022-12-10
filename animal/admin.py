from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'get_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    prepopulated_fields = {'slug': ('title',)}
    fields = ('title', 'slug', 'category', 'content', 'photo', 'get_photo', 'is_published', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at', 'get_photo')

    def get_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_photo.short_description = 'Миниатюра'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Animal, AnimalAdmin)
admin.site.register(Category, CategoryAdmin)

# Настройка админ - панели
admin.site.site_header = 'Администрирование сайта о Домашних животных'
admin.site.site_title = 'О домашних животных'
