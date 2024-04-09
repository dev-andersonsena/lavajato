from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from .modelo_carro import MODELOS_CARRO_CHOICES

class User(AbstractUser):
    telefone = models.CharField(max_length=15)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Alterado para CASCADE
    telefone = models.CharField(max_length=15)
    modelo_carro_preferido = models.CharField(max_length=20, choices=MODELOS_CARRO_CHOICES, default='')

    def __str__(self):
        return self.user.username
