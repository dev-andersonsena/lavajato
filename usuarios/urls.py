from django.urls import path
from usuarios.views import login_view, cadastro, logout, escolher_modelo, carro, tipoLavagem, calendario, home, horario, tipoLavagem2,  tipoLavagem3, tipoLavagem4, tipoLavagem5, tipoLavagem6, agendamento
from usuarios.views import tipoLavagemA, tipoLavagem2A, tipoLavagem3A, tipoLavagem4A, tipoLavagem5A, tipoLavagem6A
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('login/', login_view, name='login'),
    path('agendamento/', agendamento, name='agendamento'),
    path('cadastro', cadastro, name='cadastro'),
    path('logout', logout, name='logout'),
    path('escolher_modelo/<str:modelo>/', escolher_modelo, name='escolher_modelo'),
    path('carro', carro, name='carro'),
    path('calendario', calendario, name='calendario'),
    path('home', home, name='home'),
    path('horario', horario, name='horario'),
    path('tipolavagemHATCH', tipoLavagem, name='tipolavagemHATCH'),
    path('tipolavagemSEDAN', tipoLavagem2, name='tipolavagemSEDAN'),
    path('tipolavagemPICAPE', tipoLavagem3, name='tipolavagemPICAPE'),
    path('tipolavagemSUV', tipoLavagem4, name='tipolavagemSUV'),
    path('tipolavagemMOTO', tipoLavagem5, name='tipolavagemMOTO'),
    path('tipolavagemMOTO#2', tipoLavagem6, name='tipolavagemMOTO#2'),
    path('tipolavagemHATCH_A', tipoLavagemA, name='tipolavagemHATCH_A'),
    path('tipolavagemSUV_A', tipoLavagem2A, name='tipolavagemSUV_A'),
    path('tipolavagemSEDAN_A', tipoLavagem3A, name='tipolavagemSEDAN_A'),
    path('tipolavagemPICAPE_A', tipoLavagem4A, name='tipolavagemPICAPE_A'),
    path('tipolavagemMOTO_A',tipoLavagem5A, name='tipolavagemMOTO_A'),
    path('tipolavagemMOTO2_A',tipoLavagem6A, name='tipolavagemMOTO2_A'),





    

    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

