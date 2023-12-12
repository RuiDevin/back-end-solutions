from django.db import models

from .informacoes import SeuModelo

CONSOLE_CHOICES = [
    ('Xbox', 'Xbox 360'),
    ('Xbox', 'Xbox One Fat'),
    ('Xbox', 'Xbox One S'),
    ('Xbox', 'Xbox One X'),
    ('Play', 'Playstation 1'),
    ('Play', 'Playstation 2'),
    ('Play', 'Playstation 3 Fat 4 usb'),
    ('Play', 'Playstation 3 Fat'),
    ('Play', 'Playstation 3 Slim'),
    ('Play', 'Playstation 3 Super Slim'),
    ('Play', 'Playstation 4 Fat'),
    ('Play', 'Playstation 4 Slim'),
    ('Play', 'Playstation 4 Pro'),
    ('Play', 'Playstation 5'),
]

class Console(models.Model):
    marca_e_modelo = models.CharField(max_length=255, choices=CONSOLE_CHOICES)
    diagnostico = models.ForeignKey(SeuModelo, on_delete=models.PROTECT, null=True)
    complemento_detalhes = models.CharField(max_length=255, blank=True)
    data_e_horario = models.DateTimeField(null=True)
    
    def __str__(self):
        return f'Console - {self.marca_e_modelo}'