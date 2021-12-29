from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('contatos/', contatos, name='contatos'),
    path('api/auth/token/<int:code>/', get_access_token, name='get_access_token'),
    path('contatos/create/', create_contato, name='create_contato'),
    path('contatos/delete/<int:pk>', delete_contato, name='delete_contato'),
]