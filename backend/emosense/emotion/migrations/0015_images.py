# Generated by Django 5.0.2 on 2024-02-14 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("emotion", "0014_delete_images"),
    ]

    operations = [
        migrations.CreateModel(
            name="Images",
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
                ("image_data", models.ImageField(upload_to="images/")),
                ("captured_at", models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
