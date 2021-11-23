# Generated by Django 3.2.9 on 2021-11-23 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('telefone', models.CharField(max_length=100)),
                ('especialidade', models.CharField(max_length=100)),
            ],
        ),
    ]
