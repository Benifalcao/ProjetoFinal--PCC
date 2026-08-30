from django.db import models
from django.contrib.auth.models import User

class Usuario(User):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome or self.username