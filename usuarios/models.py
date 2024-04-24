from django.contrib.auth.models import AbstractUser
from django.db import models
from .modelo_carro import MODELOS_CARRO_CHOICES, TIPOS_LAVAGEM_CHOICES, DIA_SEMANA_CHOICES,HORARIO_SEMANA_CHOICES

class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=15)
    modelo_carro_preferido = models.CharField(max_length=20, choices=MODELOS_CARRO_CHOICES, default='')
    filial_preferida = models.CharField(max_length=100, blank=True, null=True)
    tipo_lavagem = models.CharField(max_length=100, choices=TIPOS_LAVAGEM_CHOICES, default='')
    dia_semana = models.CharField(max_length=20, choices=DIA_SEMANA_CHOICES, default='')  # Adicione este campo
    horario = models.CharField(max_length=20, choices=HORARIO_SEMANA_CHOICES, default='')  # Adicione este campo

    class Meta:
        verbose_name = 'Relatórios de Agendamento'

    def __str__(self):
        return self.user.username
    
class Agendamento(models.Model):
    usuario = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    data_agendamento = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Agendamento de {self.usuario.user.username} em {self.data_agendamento}"


#####  formação de duplas de funcionarios #####3

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    Dupla = models.CharField(max_length=100)
    colega = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.nome
#####  formação de duplas de funcionarios #####3


