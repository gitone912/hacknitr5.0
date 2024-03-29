# Generated by Django 5.0.2 on 2024-03-02 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0008_audiofile_delete_calmsongs_delete_happysongs_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="AudioRecording",
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
                ("audio_file", models.FileField(upload_to="audio_recordings/")),
            ],
        ),
    ]
