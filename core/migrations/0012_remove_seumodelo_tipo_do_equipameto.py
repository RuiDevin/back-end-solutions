# Generated by Django 4.2.7 on 2023-11-22 13:43

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0011_console"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="seumodelo",
            name="tipo_do_equipameto",
        ),
    ]
