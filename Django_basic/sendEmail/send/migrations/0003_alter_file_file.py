# Generated by Django 4.2.2 on 2023-06-14 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("send", "0002_alter_file_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="file", name="file", field=models.FileField(upload_to="upload/"),
        ),
    ]