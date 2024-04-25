from django.urls import path
from usuarios.views import login_view, cadastro, logout, escolher_modelo, carro, tipoLavagem, calendario, home, horario, tipoLavagem2,  tipoLavagem3, tipoLavagem4

urlpatterns = [
    path('login', login_view, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout', logout, name='logout'),
    path('escolher-modelo/<str:modelo>/', escolher_modelo, name='escolher_modelo'),
    path('carro', carro, name='carro'),
    path('tipolavagem', tipoLavagem, name='tipolavagem'),
    path('calendario', calendario, name='calendario'),
    path('home', home, name='home'),
    path('horario', horario, name='horario'),
    path('tipolavagem#2', tipoLavagem2, name='tipolavagem#2'),
    path('tipolavagem#3', tipoLavagem3, name='tipolavagem#3'),
    path('tipolavagem#4', tipoLavagem4, name='tipolavagem#4'),




]
