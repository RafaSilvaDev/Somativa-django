# Generated by Django 3.2.4 on 2021-11-24 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consulta', '0003_auto_20211124_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consulta',
            name='paciente_medico',
        ),
        migrations.AddField(
            model_name='consulta',
            name='paciente',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]