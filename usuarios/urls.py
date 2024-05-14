from django.urls import path
from usuarios.views import login_view, cadastro, logout, escolher_modelo, carro, tipoLavagem, calendario, home, horario, tipoLavagem2,  tipoLavagem3, tipoLavagem4, tipoLavagem5, tipoLavagem6
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('login/', login_view, name='login'),
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
    




]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

