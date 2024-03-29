# Generated by Django 5.0 on 2024-03-06 17:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_reception_doctor_alter_reception_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reception',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.doctor', verbose_name='Доктор'),
        ),
        migrations.AlterField(
            model_name='reception',
            name='services',
            field=models.ManyToManyField(blank=True, null=True, to='main.service', verbose_name='Услуги'),
        ),
    ]
