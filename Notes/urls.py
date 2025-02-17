from django.urls import path
from .views import index, foryou, itstime

urlpatterns = [
    path('', index, name='index'),
]
