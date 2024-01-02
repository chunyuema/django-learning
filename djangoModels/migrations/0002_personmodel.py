# Generated by Django 4.2 on 2024-01-02 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("djangoModels", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PersonModel",
            fields=[
                (
                    "uid",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(db_index=True, max_length=30, unique=True)),
                ("age", models.IntegerField(default=18)),
                ("is_deleted", models.BooleanField(default=False)),
            ],
        ),
    ]