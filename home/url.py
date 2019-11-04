from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contato/', views.contato, name='contato'),
    path('perfil/', views.perfil, name='perfil'),
]