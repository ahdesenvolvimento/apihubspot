from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('contatos/', contatos, name='contatos'),
    path('auth/', auth, name='auth'),
    path('api/auth/token/', get_access_token, name='get_access_token'),
    path('contatos/create/', create_contato, name='create_contato'),
]