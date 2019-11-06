from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contato/', views.contato, name='contato'),
    path('perfil/', views.perfil, name='perfil'),
    path('login/', views.login, name='login'),
    path('registrar/', views.registrar, name='registrar'),
]