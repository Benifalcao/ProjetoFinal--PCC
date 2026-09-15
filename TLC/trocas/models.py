from django.db import models

class Troca(models.Model):
    status = models.CharField(max_length=20)
    ofertantes = models.CharField(max_length=100)
    data_inicial = models.DateField()
    data_resposta = models.DateField(null=True, blank=True)
    interessado = models.CharField(max_length=100)

    # Relacionamentos N:N através das tabelas intermediárias (em apps separados)
    usuarios = models.ManyToManyField('usuario.Usuario', through='UsuarioTroca.UsuarioTroca', related_name='trocas')
    objetos = models.ManyToManyField('objetos.Objeto', through='ObjetoTroca.ObjetoTroca', related_name='trocas')

    def __str__(self):
        return f"Troca #{self.pk} - {self.status}"

