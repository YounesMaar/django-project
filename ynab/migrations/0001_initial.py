# Generated by Django 5.0.6 on 2024-05-23 10:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categorie",
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
                ("type", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="user",
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
                ("nom", models.CharField(max_length=20)),
                ("mot_de_passe", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Depense",
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
                ("montant", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date", models.DateField()),
                ("payment_method", models.CharField(max_length=100)),
                (
                    "Categorie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ynab.categorie"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="expenses",
                        to="ynab.user",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="categorie",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="categories",
                to="ynab.user",
            ),
        ),
    ]
