# Create your models here.
from django.db import models
from django.contrib.auth.models import User

  class ObjetoTroca(models.Model):
    objeto = models.ForeignKey(Objeto, on_delete=models.CASCADE)
    troca = models.ForeignKey(Troca, on_delete=models.CASCADE)
    quant = models.IntegerField()
    data_troca = models.DateField()
    observacao = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.objeto.nome} em Troca #{self.troca.pk}"