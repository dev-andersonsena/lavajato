from django.contrib.auth.models import AbstractUser
from django.db import models
from .modelo_carro import MODELOS_CARRO_CHOICES

class User(AbstractUser):
    pass

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=15)
    modelo_carro_preferido = models.CharField(max_length=20, choices=MODELOS_CARRO_CHOICES, default='')

    def __str__(self):
        return self.user.username
