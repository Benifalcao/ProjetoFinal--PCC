from django.db import models

class Troca(models.Model):
    status = models.CharField(max_length=20)
    ofertantes = models.CharField(max_length=100)
    dateInicial = models.CharField(max_length=20)
    dataRescc = models.CharField(max_length=20, null=True, blank=True)
    Interessado = models.CharField(max_length=100)

    def __str__(self):
        return f"Troca #{self.pk} - {self.status}"