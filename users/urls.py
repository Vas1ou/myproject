from django.urls import path, include
from django.views.generic import TemplateView

from .views import Register, EmailVerify, MyLoginView, MyTemplateView

urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('', include('django.contrib.auth.urls')),
    path('invalid_verify/', TemplateView.as_view(template_name='registration/invalid_verify.html'), name='invalid_verify'),
    path('register/', Register.as_view(), name='register'),
    path('confirm_email/', MyTemplateView.as_view(), name='confirm_email'),
    path('verify_email/<uidb64>/<token>/', EmailVerify.as_view(), name='verify_email'),
]
