# Generated by Django 4.2.7 on 2023-11-22 19:33

from django.db import migrations, models
import secrets


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0022_alter_celular_codigo_unico"),
    ]

    operations = [
        migrations.AlterField(
            model_name="console",
            name="codigo_unico",
            field=models.CharField(default=secrets.token_urlsafe, max_length=43, unique=True),
        ),
        migrations.AlterField(
            model_name="desktop",
            name="codigo_unico",
            field=models.CharField(default=secrets.token_urlsafe, max_length=43, unique=True),
        ),
        migrations.AlterField(
            model_name="notebook",
            name="codigo_unico",
            field=models.CharField(default=secrets.token_urlsafe, max_length=43, unique=True),
        ),
    ]
