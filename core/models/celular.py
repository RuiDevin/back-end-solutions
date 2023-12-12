import secrets

from django.db import models 

from .informacoes import SeuModelo

IPHONE_APPLE_CHOICES = [
    ('Apple 2014', 'Iphone 6'),
    ('Apple 2014', 'Iphone 6 Plus'),
    ('Apple 2015', 'Iphone 6s'),
    ('Apple 2015', 'Iphone 6s Plus'),
    ('Apple 2016', 'Iphone 7'),
    ('Apple 2016', 'Iphone 7 Plus'),
    ('Apple 2017', 'Iphone 8'),
    ('Apple 2017', 'Iphone 8 Plus'),
    ('Apple 2017', 'Iphone X'),
    ('Apple 2018', 'Iphone Xs'),
    ('Apple 2018', 'Iphone Xr'),
    ('Apple 2018', 'Iphone XS MAX'),
    ('Apple 2019', 'Iphone 11'),
    ('Apple 2019', 'Iphone 11 Pro'),
    ('Apple 2019', 'Iphone 11 Pro Max'),
    ('Apple 2020', 'Iphone 12 Mini'),
    ('Apple 2020', 'Iphone 12'),
    ('Apple 2020', 'Iphone 12 Pro'),
    ('Apple 2020', 'Iphone 12 Pro Max'),
    ('Apple 2021', 'Iphone 13 Mini'),
    ('Apple 2021', 'Iphone 13'),
    ('Apple 2021', 'Iphone 13 Pro'),
    ('Apple 2021', 'Iphone 13 Pro Max'),
    ('Apple 2022', 'Iphone 14 Mini'),
    ('Apple 2022', 'Iphone 14'),
    ('Apple 2022', 'Iphone 14 Pro'),
    ('Apple 2022', 'Iphone 14 Pro Max'),
    ('Apple 2023', 'Iphone 15'),
    ('Apple 2023', 'Iphone 15 Plus'),
    ('Apple 2023', 'Iphone 15 Pro'),
    ('Apple 2023', 'Iphone 15 Pro Max'),
]

SAMSUNG_CHOICES = [
    ('Samsung A', 'Samsung Galaxy A'),
    ('Samsung M', 'Samsung Galaxy M'),
    ('Samsung J', 'Samsung Galaxy J'),
    ('Samsung S', 'Samsung Galaxy S'),
    ('Samsung Z-Fold', 'Samsung Galaxy Z-Fold'),
    ('Samsung Z-Flip', 'Samsung Galaxy Z-Flip'),
    ('Samsung Tab A', 'Samsung Galaxy Tab A'),
    ('Samsung Tab S', 'Samsung Galaxy Tab S'),
]

XIAOMI_CHOICES = [
    ('Xiaomi', 'Xiaomi Redmi'),
    ('Xiaomi', 'Xiaomi Redmi Note'),
    ('Xiaomi', 'Xiaomi Poco'),
    ('Xiaomi', 'Xiaomi Mi'),
]

MOTOROLA_CHOICES = [
    ('Motorola', 'Motorola G'),
    ('Motorola', 'Motorola E'),
    ('Motorola', 'Motorola Raze'),
    ('Motorola', 'Motorola Z'),
    ('Motorola', 'Motorola One'),
]

MODELO_CHOICES = MOTOROLA_CHOICES + IPHONE_APPLE_CHOICES + SAMSUNG_CHOICES + XIAOMI_CHOICES

class Celular(models.Model):
    modelo_e_marca = models.CharField(max_length=255, choices=MODELO_CHOICES)
    diagnostico = models.ForeignKey(SeuModelo, on_delete=models.PROTECT, null=True)
    complemento_detalhes = models.CharField(max_length=255, blank=True)
    data_e_horario = models.DateTimeField(null=True)
    codigo_unico = models.CharField(max_length=43, unique=True, default=secrets.token_urlsafe)

    def save(self, *args, **kwargs):
        if not self.codigo_unico:
            self.codigo_unico = secrets.token_urlsafe(16)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Desktop - {self.codigo_unico}'
