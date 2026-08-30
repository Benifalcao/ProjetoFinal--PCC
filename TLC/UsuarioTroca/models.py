from django.db import models

class UsuarioTroca(models.Model):
    usuario = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE)
    troca = models.ForeignKey('trocas.Troca', on_delete=models.CASCADE)
    status = models.CharField(max_length=20)
    dataInicio = models.CharField(max_length=20)
    protocolo = models.CharField(max_length=100)
    DataRenovacao = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"Usuário {self.usuario.username} na Troca #{self.troca.pk}"

    class Meta:
        verbose_name = "Usuário da Troca"
        verbose_name_plural = "Usuários das Trocas"