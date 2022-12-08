from django.urls import path

from .views import *

urlpatterns = [
    path('', AnimalHome.as_view(), name='home'),
    path('category/<slug:category_slug>/', AnimalCategory.as_view(), name='categories'),
    path('post/<slug:post_slug>/', ShowAnimal.as_view(), name='post'),
    path('addpage/', AddPage.as_view(), name='addpage'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user , name='logout'),
    path('about/', about, name='about'),
    path('feedback/', feedback, name='feedback'),
]
