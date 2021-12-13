# Generated by Django 3.2.9 on 2021-12-12 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaclinica', '0013_medicamentos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jornadas',
            fields=[
                ('idJ', models.AutoField(primary_key=True, serialize=False)),
                ('nombrej', models.CharField(max_length=100, verbose_name='Nombre')),
                ('cargoj', models.CharField(max_length=30, verbose_name='Cargo')),
                ('fechaj', models.CharField(max_length=10, verbose_name='Fecha')),
                ('horaen', models.CharField(max_length=10, verbose_name='Hora de entrada')),
                ('horasa', models.CharField(max_length=10, verbose_name='Hora de salida')),
                ('horasex', models.CharField(max_length=10, verbose_name='Horas extras')),
            ],
        ),
    ]