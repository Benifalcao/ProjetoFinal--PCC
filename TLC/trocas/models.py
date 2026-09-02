from django.db import models


class UsuarioTroca(models.Model):
    usuario = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE, related_name='rel_usuario_trocas')
    troca = models.ForeignKey('Troca', on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    data_inicio = models.DateField()
    protocolo = models.CharField(max_length=50)
    data_renovacao = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.usuario.nome} - Troca #{self.troca.pk}"


class ObjetoTroca(models.Model):
    objeto = models.ForeignKey('objetos.Objeto', on_delete=models.CASCADE)
    troca = models.ForeignKey('Troca', on_delete=models.CASCADE)
    quant = models.IntegerField()
    data_troca = models.DateField()
    observacao = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.objeto.nome} em Troca #{self.troca.pk}"


class Troca(models.Model):
    status = models.CharField(max_length=20)
    ofertantes = models.CharField(max_length=100)
    data_inicial = models.DateField()
    data_resposta = models.DateField(null=True, blank=True)
    interessado = models.CharField(max_length=100)

    # Relacionamentos N:N através das tabelas intermediárias
    usuarios = models.ManyToManyField('usuario.Usuario', through='UsuarioTroca', related_name='trocas')
    objetos = models.ManyToManyField('objetos.Objeto', through='ObjetoTroca', related_name='trocas')

    def __str__(self):
        return f"Troca #{self.pk} - {self.status}"