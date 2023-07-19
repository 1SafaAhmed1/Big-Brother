from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('register_success/', views.register_success_view, name='register_success'),
]