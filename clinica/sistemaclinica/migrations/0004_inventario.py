# Generated by Django 3.2.9 on 2021-12-10 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaclinica', '0003_alter_recetas_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('idI', models.AutoField(primary_key=True, serialize=False)),
                ('equipo', models.CharField(max_length=100, verbose_name='Equipo')),
                ('costo', models.CharField(max_length=10, verbose_name='Costo')),
                ('vidautil', models.CharField(max_length=10, verbose_name='Vida util en Años')),
                ('vidameses', models.CharField(max_length=100, verbose_name='Vida util en Meses')),
                ('cantidad', models.CharField(max_length=10, verbose_name='Cantidad')),
            ],
        ),
    ]