# Generated by Django 4.2.7 on 2024-04-04 23:49

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("settings", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="About",
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
                ("title", models.CharField(max_length=155, verbose_name="Заголовка")),
                (
                    "descriptions",
                    ckeditor.fields.RichTextField(verbose_name="Описание"),
                ),
            ],
            options={
                "verbose_name_plural": "О нас",
            },
        ),
    ]
