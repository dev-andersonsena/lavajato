from django.urls import path
from usuarios.views import login_view, cadastro, logout, escolher_modelo, carro, tipoLavagem, calendario, home, horario, tipoLavagem2,  tipoLavagem3, tipoLavagem4

urlpatterns = [
    path('login', login_view, name='login'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout', logout, name='logout'),
    path('escolher-modelo/<str:modelo>/', escolher_modelo, name='escolher_modelo'),
    path('carro', carro, name='carro'),
    path('tipolavagemHATCH', tipoLavagem, name='tipolavagemHATCH'),
    path('calendario', calendario, name='calendario'),
    path('home', home, name='home'),
    path('horario', horario, name='horario'),
    path('tipolavagemSEDAN', tipoLavagem2, name='tipolavagemSEDAN'),
    path('tipolavagemPICAPE', tipoLavagem3, name='tipolavagemPICAPE'),
    path('tipolavagemSUV', tipoLavagem4, name='tipolavagemSUV'),




]
