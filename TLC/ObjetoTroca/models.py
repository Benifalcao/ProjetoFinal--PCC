from django.db import models

class ObjetoTroca(models.Model):
    objeto = models.ForeignKey('objetos.Objeto', on_delete=models.CASCADE)
    troca = models.ForeignKey('trocas.Troca', on_delete=models.CASCADE)
    quant = models.IntegerField()
    data_troca = models.CharField(max_length=20)
    obsevação = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Objeto #{self.objeto.pk} na Troca #{self.troca.pk}"

    class Meta:
        verbose_name = "Objeto da Troca"
        verbose_name_plural = "Objetos das Trocas"