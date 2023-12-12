
from django.db import models

from .informacoes import SeuModelo

class Notebook(models.Model):
    diagnostico = models.ForeignKey(SeuModelo, on_delete=models.PROTECT, null=True)
    complemento_detalhes = models.CharField(max_length=255, blank=True)
    data_e_horario = models.DateTimeField(null=True)

    def __str__(self):
        return f'Notebook - {self.diagnostico}'