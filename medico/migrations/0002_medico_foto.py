# Generated by Django 3.2.9 on 2021-11-23 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medico', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medico',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='media/medicos/fotos'),
        ),
    ]
