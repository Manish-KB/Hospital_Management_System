# Generated by Django 4.0.6 on 2023-01-08 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_appointment_app_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='app_date',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='app_time',
        ),
        migrations.AddField(
            model_name='appointment',
            name='app_date_time',
            field=models.DateField(blank=True, null=True),
        ),
    ]
