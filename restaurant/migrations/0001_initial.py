# Generated by Django 5.0 on 2023-12-21 04:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigIntegerField(
                        primary_key=True,
                        serialize=False,
                        validators=[
                            django.core.validators.MaxValueValidator(99999999999)
                        ],
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "no_of_guests",
                    models.IntegerField(
                        validators=[django.core.validators.MaxValueValidator(999999)]
                    ),
                ),
                ("bookingDate", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="Menu",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        primary_key=True,
                        serialize=False,
                        validators=[django.core.validators.MaxValueValidator(99999)],
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("inventory", models.SmallIntegerField()),
            ],
        ),
    ]