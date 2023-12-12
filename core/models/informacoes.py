from django.db import models

class SubOpcaoEscolha(models.TextChoices):
    SUB_OPCAO_1 = 'Oxidação', 'Agua'
    SUB_OPCAO_2 = 'Impacto', 'Queda do chao'
    SUB_OPCAO_3 = 'Marisia', 'Cidade Litoranea'
    SUB_OPCAO_4 = 'Mau uso', 'Queda acidental'
    SUB_OPCAO_5 = 'Tentaiva de reparo', 'Mexeram antes'

class SeuModelo(models.Model):
    diagnostico = models.CharField(
        max_length=20,
        choices=SubOpcaoEscolha.choices,
        default=SubOpcaoEscolha.SUB_OPCAO_1,
    )
    def __str__(self):
        return self.diagnostico

    