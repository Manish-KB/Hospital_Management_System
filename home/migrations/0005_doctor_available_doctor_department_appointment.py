# Generated by Django 4.0.6 on 2023-01-08 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_patient_blood_group_patient_health_conditions_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='department',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateField(auto_now=True)),
                ('app_date', models.DateTimeField(blank=True, null=True)),
                ('patientName', models.CharField(blank=True, max_length=20, null=True)),
                ('doctorName', models.CharField(blank=True, max_length=40, null=True)),
                ('patientId', models.PositiveIntegerField(null=True)),
                ('doctorId', models.PositiveIntegerField(null=True)),
                ('symptoms', models.TextField(blank=True, max_length=100, null=True)),
                ('status', models.BooleanField(blank=True, default=False, null=True)),
                ('doctor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.doctor')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.patient')),
            ],
        ),
    ]
