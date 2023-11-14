from django.db import models

ORDEM_CATEGORIA = [
    ('CELULAR' , 'Ordem_celular'),
    ('DESKTOP' , 'Ordem_desktop'),
    ('NOTEBOOK' , 'Ordem_notebook'),
    ('CONSOLE' , 'Ordem_console'),
]

class Ordem(models.Model):
    titulo = models.TextField()
    data = models.DateTimeField()
    ordem = models.CharField(max_length=255, choices=ORDEM_CATEGORIA)