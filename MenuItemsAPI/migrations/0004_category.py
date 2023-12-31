# Generated by Django 4.2.2 on 2023-07-27 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("MenuItemsAPI", "0003_menuitem_category"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=100)),
                ("slug", models.SlugField(default=1, max_length=100)),
            ],
        ),
    ]
