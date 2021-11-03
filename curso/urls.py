from django.urls import path
from .views import curso

urlpatterns = [
    path('', curso, name='curso'),
]
