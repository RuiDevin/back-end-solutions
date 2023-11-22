# models.py
from django.db import models

from .desktop import Desktop
from .celular import Celular
from .console import Console
from .notebook import Notebook

ORDEM_CATEGORIA = [
    ('CELULAR', 'Ordem celular'),
    ('DESKTOP', 'Ordem desktop'),
    ('NOTEBOOK', 'Ordem notebook'),
    ('CONSOLE', 'Ordem console'),
]

class Ordem(models.Model):
    titulo = models.TextField()
    data = models.DateTimeField()
    ordem = models.CharField(max_length=255, choices=ORDEM_CATEGORIA)
    
    def get_info(self):
        if self.ordem == 'CELULAR':
            return Celular.objects.get(ordem=self)
        elif self.ordem == 'DESKTOP':
            return Desktop.objects.get(ordem=self)
        elif self.ordem == 'NOTEBOOK':
            return Notebook.objects.get(ordem=self)
        elif self.ordem == 'CONSOLE':
            return Console.objects.get(ordem=self)
        else:
            return None

    def __str__(self):
        return f'{self.ordem} - {self.titulo}'
