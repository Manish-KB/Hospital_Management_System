# Generated by Django 4.0.6 on 2023-02-26 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0035_accountant_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountant',
            name='dob',
            field=models.DateField(default=None, max_length=8, null=True),
        ),
    ]
