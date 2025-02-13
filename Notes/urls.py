from django.urls import path
from .views import index, foryou

urlpatterns = [
    path('', index, name='index'),
    path('foryou', foryou, name='foryou'),
]
