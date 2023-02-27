# Generated by Django 4.1.5 on 2023-02-17 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_food_delete_cartitem_delete_list"),
    ]

    operations = [
        migrations.CreateModel(
            name="YOLOv5Result",
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
                ("image", models.ImageField(upload_to="images/")),
                ("result", models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name="Food",
        ),
    ]