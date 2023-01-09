from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', AnimalHome.as_view(), name='home'),
    path('category/<slug:category_slug>/', cache_page(60)(AnimalCategory.as_view()), name='categories'),
    path('post/<slug:post_slug>/', cache_page(60)(ShowAnimal.as_view()), name='post'),
    path('addpage/', AddPage.as_view(), name='addpage'),
    # path('register/', RegisterUser.as_view(), name='register'),
    # path('login/', LoginUser.as_view(), name='login'),
    # path('logout/', logout_user , name='logout'),
    path('about/', About.as_view(), name='about'),
    path('feedback/', ContactFormView.as_view(), name='feedback'),
]
