# Generated by Django 4.0.6 on 2023-02-26 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0034_appointment_istatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountant',
            name='address',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
