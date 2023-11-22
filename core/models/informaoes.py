from django.db import models

TIPO_DE_EQUIPAMENTOS_CHOICES = [
    ('SmartPhone', 'Celular'),
    ('PC', 'Desktop'),
    ('PC', 'Notebook'),
    ('Console', 'Video Game'),
]

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

MARCA_CELULAR_CHOICES = [
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
    ('Samsung', 'Linha A'),
    ('Samsung', 'Linha M'),
    ('Samsung', 'Linha J'),
    ('Samsung', 'Linha S'),
    ('Samsung', 'Linha Z-Fold'),
    ('Samsung', 'Linha Z-Flip'),
    ('Samsung', 'Linha Tab A'),
    ('Samsung', 'Linha Tab S'),
    ('Motorola', 'Linha G'),
    ('Motorola', 'Linha E'),
    ('Motorola', 'Linha Raze'),
    ('Motorola', 'Linha Z'),
    ('Motorola', 'Linha One'),
    ('Xiaomi', 'Linha Redmi'),
    ('Xiaomi', 'Linha Redmi Note'),
    ('Xiaomi', 'Linha Poco'),
    ('Xiaomi', 'Linha Mi'),
]

class OpcaoEscolha(models.TextChoices):
    OPCAO_1 = 'Smarthphone', 'Celular'
    OPCAO_2 = 'Desktop', 'Computador'
    OPCAO_3 = 'Notebook', 'Notebook'
    OPCAO_4 = 'Console', 'Video Game'

class SubOpcaoEscolha(models.TextChoices):
    SUB_OPCAO_1 = 'Oxidação', 'Agua'
    SUB_OPCAO_2 = 'Impacto', 'Queda do chao'
    SUB_OPCAO_3 = 'Marisia', 'Cidade Litoranea'
    SUB_OPCAO_4 = 'Mau uso', 'Queda acidental'
    SUB_OPCAO_5 = 'Tentaiva de reparo', 'Mexeram antes'

class SeuModelo(models.Model):
    tipo_do_equipameto = models.CharField(
        max_length=20,
        choices=OpcaoEscolha.choices,
        default=OpcaoEscolha.OPCAO_1,
    )
    diagnostico = models.CharField(
        max_length=20,
        choices=SubOpcaoEscolha.choices,
        default=SubOpcaoEscolha.SUB_OPCAO_1,
    )

    