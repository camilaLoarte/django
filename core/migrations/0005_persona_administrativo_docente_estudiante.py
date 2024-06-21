# Generated by Django 5.0.6 on 2024-06-03 16:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0004_asignatura_malla_asignatura_semestre"),
    ]

    operations = [
        migrations.CreateModel(
            name="Persona",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre",
                    models.CharField(
                        max_length=100, verbose_name="Registra los nombres"
                    ),
                ),
                (
                    "apellidos",
                    models.CharField(
                        max_length=100, verbose_name="Registra los apellidos"
                    ),
                ),
                (
                    "cedula_ruc",
                    models.CharField(
                        max_length=13,
                        verbose_name="Ingresa el numero de identificacion",
                    ),
                ),
                (
                    "telefono",
                    models.CharField(max_length=9, verbose_name="Telefono de casa"),
                ),
                (
                    "celular",
                    models.CharField(max_length=10, verbose_name="Numero de celular"),
                ),
                (
                    "correo",
                    models.CharField(max_length=100, verbose_name="Ingrese el email"),
                ),
                (
                    "fecha_Nacimiento",
                    models.DateField(verbose_name="Fecha de Nacimiento"),
                ),
                ("edad", models.DateField(verbose_name="Edad")),
                (
                    "estado_civil",
                    models.CharField(
                        choices=[
                            ("Soltero", "Soltero"),
                            ("Casado", "Casado"),
                            ("Divorciado", "Divorciado"),
                            ("viudo", "Viudo"),
                        ],
                        max_length=100,
                        verbose_name="Estado Civil",
                    ),
                ),
                (
                    "genero",
                    models.CharField(
                        choices=[("masculino", "Masculino"), ("femenino", "Femenino")],
                        max_length=100,
                        verbose_name="Seleccione el genero",
                    ),
                ),
                (
                    "sexo",
                    models.CharField(
                        choices=[("hombre", "Hombre"), ("mujer", "Mujer")],
                        max_length=100,
                        verbose_name="Nombre",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Administrativo",
            fields=[
                (
                    "persona_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.persona",
                    ),
                ),
                (
                    "correo_institucional",
                    models.EmailField(
                        max_length=100, verbose_name="Correo Institucional"
                    ),
                ),
            ],
            bases=("core.persona",),
        ),
        migrations.CreateModel(
            name="Docente",
            fields=[
                (
                    "persona_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.persona",
                    ),
                ),
                (
                    "correo_institucional",
                    models.EmailField(
                        max_length=100, verbose_name="Correo Institucional"
                    ),
                ),
            ],
            bases=("core.persona",),
        ),
        migrations.CreateModel(
            name="Estudiante",
            fields=[
                (
                    "persona_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.persona",
                    ),
                ),
                (
                    "codigo",
                    models.CharField(max_length=5, verbose_name="Ingresa el codigo"),
                ),
                (
                    "correo_institucional",
                    models.EmailField(
                        max_length=100, verbose_name="Correo Institucional"
                    ),
                ),
            ],
            bases=("core.persona",),
        ),
    ]
