
# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Objeto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="objetos")
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    valor_avaliacao = models.IntegerField()
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Troca(models.Model):
    status = models.CharField(max_length=20)
    ofertantes = models.CharField(max_length=100)
    data_inicial = models.DateField()
    data_resposta = models.DateField(null=True, blank=True)
    interessado = models.CharField(max_length=100)
    objetos = models.ManyToManyField(Objeto, related_name="trocas")

    def __str__(self):
        return f"Troca #{self.pk} - {self.status}"