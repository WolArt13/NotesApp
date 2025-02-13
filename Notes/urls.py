from django.urls import path
from .views import index, foryou, itstime

urlpatterns = [
    path('', index, name='index'),
    path('foryou', foryou, name='foryou'),
    path('itstime', itstime, name='itstime'),
]
