import secrets

from django.db import models

from .informacoes import SeuModelo

class Desktop(models.Model):
    diagnostico = models.ForeignKey(SeuModelo, on_delete=models.PROTECT, null=True)
    complemento_detalhes = models.CharField(max_length=255, blank=True)
    data_e_horario = models.DateTimeField(null=True)
    codigo_unico = models.CharField(max_length=43, unique=True, default=secrets.token_urlsafe)

    def save(self, *args, **kwargs):
        # Verifica se o código único já foi definido
        if not self.codigo_unico:
            self.codigo_unico = secrets.token_urlsafe(16)  # Você pode ajustar o tamanho conforme necessário
        super().save(*args, **kwargs)
