from django.urls import path

from .views import *

urlpatterns = [
    path('', AnimalHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('feedback/', feedback, name='feedback'),
    path('addpage/', AddPage.as_view(), name='addpage'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('post/<slug:post_slug>/', ShowAnimal.as_view(), name='post'),
    path('category/<slug:category_slug>/', AnimalCategory.as_view(), name='categories'),
]
