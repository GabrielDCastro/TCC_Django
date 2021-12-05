from django.urls import path
from . import views

urlpatterns = [
    path('cursos/', views.cursos, name='cursos'),
    path('cursos/<int:fk>/', views.details, name='details'),
    path('aulas/<int:pk>/', views.details, name='lessons'),
]