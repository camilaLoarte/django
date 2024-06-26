# Generated by Django 5.0.6 on 2024-06-03 16:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0003_malla_carrera_malla_semestres"),
    ]

    operations = [
        migrations.AddField(
            model_name="asignatura",
            name="malla",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                to="core.malla",
                verbose_name="Selecciona la Malla",
            ),
        ),
        migrations.AddField(
            model_name="asignatura",
            name="semestre",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="core.semestre",
                verbose_name="Agregar el semestre",
            ),
        ),
    ]
