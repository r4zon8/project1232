# Generated by Django 4.1.4 on 2023-02-26 18:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("pos", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="salesitems",
            name="sale_id",
        ),
        migrations.DeleteModel(
            name="Sales",
        ),
    ]
