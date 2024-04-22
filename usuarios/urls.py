from django.urls import path
from usuarios.views import login_view, cadastro, logout, escolher_modelo, carro, tipoLavagem, calendario, home, horario

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




]
