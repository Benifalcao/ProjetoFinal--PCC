from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class Mensagem(models.Model):
    troca = models.ForeignKey('trocas.Troca', on_delete=models.CASCADE, related_name='mensagens')
    remetente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mensagens_enviadas')
    texto = models.TextField()
    criada_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['criada_em']
        verbose_name = "Mensagem"
        verbose_name_plural = "Mensagens"

    def nome_remetente(self):
        try:
            return self.remetente.usuario.nome or self.remetente.username
        except ObjectDoesNotExist:
            return self.remetente.username

    def __str__(self):
        return f"Troca #{self.troca_id} - {self.nome_remetente()}"

# Create your models here.
