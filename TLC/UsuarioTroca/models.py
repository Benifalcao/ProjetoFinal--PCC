# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class UsuarioTroca(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    troca = models.ForeignKey(Troca, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario.nome} - Troca #{self.troca.pk}"