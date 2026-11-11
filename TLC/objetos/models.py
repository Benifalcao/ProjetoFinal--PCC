from django.db import models


class Objeto(models.Model):
    usuario = models.ForeignKey(
        'usuario.Usuario',
        on_delete=models.CASCADE,
        related_name='objetos'
    )
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    valor_avaliacao = models.IntegerField()
    status = models.CharField(max_length=20)
    imagem = models.ImageField(
        upload_to='objetos/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.nome
