from django.db import models 
from .informaoes import SeuModelo

IPHONE_APPLE_CHOICES = [
    ('Apple', 'Iphone 6'),
    ('Apple', 'Iphone 6 Plus'),
    ('Apple', 'Iphone 6s'),
    ('Apple', 'Iphone 6s Plus'),
    ('Apple', 'Iphone 7'),
    ('Apple', 'Iphone 7 Plus'),
    ('Apple', 'Iphone 8'),
    ('Apple', 'Iphone 8 Plus'),
    ('Apple', 'Iphone X'),
    ('Apple', 'Iphone Xs'),
    ('Apple', 'Iphone Xr'),
    ('Apple', 'Iphone XS MAX'),
    ('Apple', 'Iphone 11'),
    ('Apple', 'Iphone 11 Pro'),
    ('Apple', 'Iphone 11 Pro Max'),
    ('Apple', 'Iphone 12 Mini'),
    ('Apple', 'Iphone 12'),
    ('Apple', 'Iphone 12 Pro'),
    ('Apple', 'Iphone 12 Pro Max'),
    ('Apple', 'Iphone 13 Mini'),
    ('Apple', 'Iphone 13'),
    ('Apple', 'Iphone 13 Pro'),
    ('Apple', 'Iphone 13 Pro Max'),
    ('Apple', 'Iphone 14 Mini'),
    ('Apple', 'Iphone 14'),
    ('Apple', 'Iphone 14 Pro'),
    ('Apple', 'Iphone 14 Pro Max'),
    ('Apple', 'Iphone 15'),
    ('Apple', 'Iphone 15 Plus'),
    ('Apple', 'Iphone 15 Pro'),
    ('Apple', 'Iphone 15 Pro Max'),
]

SAMSUNG_CHOICES = [
    ('Samsung', 'Samsung Galaxy A'),
    ('Samsung', 'Samsung Galaxy M'),
    ('Samsung', 'Samsung Galaxy J'),
    ('Samsung', 'Samsung Galaxy S'),
    ('Samsung', 'Samsung Galaxy Z-Fold'),
    ('Samsung', 'Samsung Galaxy Z-Flip'),
    ('Samsung', 'Samsung Galaxy Tab A'),
    ('Samsung', 'Samsung Galaxy Tab S'),
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

    def __str__(self):
        return self.modelo_e_marca
