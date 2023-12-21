# Generated by Django 5.0 on 2023-12-21 04:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menu",
            name="inventory",
            field=models.IntegerField(
                validators=[django.core.validators.MaxValueValidator(99999)]
            ),
        ),
    ]
