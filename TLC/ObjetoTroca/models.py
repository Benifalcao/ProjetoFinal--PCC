# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class UsuarioTroca(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    troca = models.ForeignKey(Troca, on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    data_inicio = models.DateField()
    protocolo = models.CharField(max_length=50)
    data_renovacao = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.usuario.nome} - Troca #{self.troca.pk}"
