# Generated by Django 4.2.7 on 2023-11-22 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0016_remove_seumodelo_complemento_detalhes_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Notebook",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("complemento_detalhes", models.CharField(blank=True, max_length=255)),
                ("data_e_horario", models.DateTimeField(null=True)),
                (
                    "diagnostico",
                    models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to="core.seumodelo"),
                ),
            ],
        ),
    ]