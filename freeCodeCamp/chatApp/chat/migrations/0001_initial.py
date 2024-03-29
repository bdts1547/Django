# Generated by Django 4.2.1 on 2023-06-10 12:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Message",
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
                ("value", models.CharField(max_length=1000000)),
                (
                    "date",
                    models.DateTimeField(
                        blank=True,
                        default=datetime.datetime(2023, 6, 10, 19, 40, 11, 814960),
                    ),
                ),
                ("user", models.CharField(max_length=1000000)),
                ("room", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Room",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
    ]
