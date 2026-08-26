# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Troca(models.Model):
    status = models.CharField(max_length=20)
    ofertantes = models.CharField(max_length=100)
    data_inicial = models.DateField()
    data_resposta = models.DateField(null=True, blank=True)
    interessado = models.CharField(max_length=100)
    objetos = models.ManyToManyField(Objeto, related_name="trocas")

    def __str__(self):
        return f"Troca #{self.pk} - {self.status}"

        usuarios = models.ManyToManyField(Usuario, through='UsuarioTroca', related_name='trocas')
    objetos = models.ManyToManyField(Objeto, through='ObjetoTroca', related_name='trocas')

    def __str__(self):
        return f"Troca #{self.pk} - {self.status}"




