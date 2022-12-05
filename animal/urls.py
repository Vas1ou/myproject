from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('feedback/', feedback, name='feedback'),
    path('addpage/', addpage, name='addpage'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<slug:category_slug>/', get_category, name='categories'),
]
