# Generated by Django 3.2.4 on 2021-11-24 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0007_medico_formacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medico',
            name='especialidade',
        ),
    ]
