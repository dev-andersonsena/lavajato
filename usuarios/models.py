from django.contrib.auth.models import AbstractUser
from django.db import models
from .modelo_carro import MODELOS_CARRO_CHOICES

class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=15)
    modelo_carro_preferido = models.CharField(max_length=20, choices=MODELOS_CARRO_CHOICES, default='')
    filial_preferida = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.user.username

#####  formação de duplas de funcionarios #####3

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    Dupla = models.CharField(max_length=100)
    colega = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.nome
#####  formação de duplas de funcionarios #####3


####   tipos de lavagem #######

class TipoLavagem(models.Model):
    tipo_lavagem = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

###### fim tipo lavagem ###########