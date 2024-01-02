# Generated by Django 4.2 on 2024-01-02 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("djangoModels", "0002_personmodel"),
    ]

    operations = [
        migrations.AddField(
            model_name="personmodel",
            name="height",
            field=models.DecimalField(decimal_places=2, default=150.0, max_digits=5),
        ),
        migrations.AddField(
            model_name="personmodel",
            name="self_intro",
            field=models.TextField(blank=True, null=True),
        ),
    ]
