# Generated by Django 4.1.4 on 2023-02-26 16:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboard", "0010_alter_appointment_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="prescription",
            name="date_end",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="prescription",
            name="date_start",
            field=models.DateField(blank=True, null=True),
        ),
    ]
