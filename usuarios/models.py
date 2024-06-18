from django.contrib.auth.models import AbstractUser
from django.db import models
from .modelo_carro import MODELOS_CARRO_CHOICES, TIPOS_LAVAGEM_CHOICES, DIA_SEMANA_CHOICES,HORARIO_SEMANA_CHOICES
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django.utils import timezone

class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=11)
    veiculo = models.CharField(max_length=50, blank=True, null=True)  # Alterando o nome do campo para veiculo
    modelo_carro_preferido = models.CharField(max_length=20, choices=MODELOS_CARRO_CHOICES, default='')
    filial_preferida = models.CharField(max_length=100, blank=True, null=True)
    tipo_lavagem = models.CharField(max_length=100, choices=TIPOS_LAVAGEM_CHOICES, default='')
    lavagem_adicional = models.CharField(max_length=100, choices=TIPOS_LAVAGEM_CHOICES, default='')
    dia_semana = models.CharField(max_length=20, choices=DIA_SEMANA_CHOICES, default='')
    horario = models.CharField(max_length=20, choices=HORARIO_SEMANA_CHOICES, default='')
    data_atual = models.DateField(null=True, blank=True)  # Adicionando o campo de data atual


    class Meta:
        verbose_name = 'Relatórios de Agendamento'

    def __str__(self):
        return self.user.username


    
class Semana(models.Model):
    numero_semana = models.PositiveSmallIntegerField(unique=True)
    horario = models.CharField(max_length=20, choices=HORARIO_SEMANA_CHOICES)



#####  formação de duplas de funcionarios #####3
class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    chave = models.CharField("Dupla", max_length=100, blank=True, null=True)
    Parceiro = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='duplas')

    def __str__(self):
        return self.nome

    def get_dupla(self):
        if self.Parceiro:
            return self.chave 
        return "Funcionário"
    def get_parceiro_nome(self):
        return self.Parceiro.nome if self.Parceiro else ''
    

class Agendamento(models.Model):
    user_profile = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    data_agendamento = models.DateField()
    horario = models.CharField(max_length=20, choices=HORARIO_SEMANA_CHOICES)

    def __str__(self):
        return f"Agendamento de {self.user_profile.user.username} com {self.funcionario.chave} em {self.data_agendamento}"
    
    class Meta:
        verbose_name = 'Relatório de Serviço'