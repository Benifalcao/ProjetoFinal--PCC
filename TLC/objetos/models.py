from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
# Create your models here.
class Objeto(models.Model):
    
    usuario = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE, related_name='objetos')
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    valor_avaliacao = models.IntegerField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.nome