import secrets
from django.db import models

from .informaoes import SeuModelo

class Notebook(models.Model):
    diagnostico = models.ForeignKey(SeuModelo, on_delete=models.PROTECT, null=True)
    complemento_detalhes = models.CharField(max_length=255, blank=True)
    data_e_horario = models.DateTimeField(null=True)
    codigo_unico = models.CharField(max_length=43, unique=True, default=secrets.token_urlsafe)

    def save(self, *args, **kwargs):
        if not self.codigo_unico:
            self.codigo_unico = secrets.token_urlsafe(16)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Notebook - {self.codigo_unico}'