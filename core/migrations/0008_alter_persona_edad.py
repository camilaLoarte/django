# Generated by Django 5.0.6 on 2024-06-05 15:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0007_rename_periodoacadémico_periodoacademico_matricula"),
    ]

    operations = [
        migrations.AlterField(
            model_name="persona",
            name="edad",
            field=models.IntegerField(verbose_name="Edad"),
        ),
    ]
