# Generated by Django 3.2.9 on 2021-12-08 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('idPaciente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('direccion', models.CharField(max_length=100, verbose_name='Direccion')),
                ('edad', models.CharField(max_length=10, verbose_name='Edad')),
                ('dui', models.CharField(max_length=15, verbose_name='Dui')),
                ('telefono', models.CharField(max_length=10, verbose_name='Telefono')),
            ],
        ),
    ]