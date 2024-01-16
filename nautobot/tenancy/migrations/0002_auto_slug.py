# Generated by Django 3.1.13 on 2021-08-05 03:23

from django.db import migrations

import nautobot.core.models.fields


class Migration(migrations.Migration):
    dependencies = [
        ("tenancy", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tenant",
            name="slug",
            field=nautobot.core.models.fields.AutoSlugField(
                blank=True, max_length=100, populate_from="name", unique=True
            ),
        ),
        migrations.AlterField(
            model_name="tenantgroup",
            name="slug",
            field=nautobot.core.models.fields.AutoSlugField(
                blank=True, max_length=100, populate_from="name", unique=True
            ),
        ),
    ]
