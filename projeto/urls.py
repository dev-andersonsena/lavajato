from django.urls import path
from .views import index, carro

urlpatterns = [
    path('', index, name='index'),
    #path('imagem/<int:foto_id>', imagem, name='imagem'),

]