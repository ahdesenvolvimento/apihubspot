from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('contatos/', contatos, name='contatos'),
    path('auth/', auth, name='auth'),
]