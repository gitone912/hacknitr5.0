# Generated by Django 4.1.11 on 2024-02-09 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_capturedimage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="capturedimage",
            name="image",
            field=models.ImageField(upload_to="media/"),
        ),
    ]