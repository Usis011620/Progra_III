# Generated by Django 3.2.9 on 2021-12-11 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaclinica', '0010_alter_citas_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citas',
            name='fechac',
            field=models.CharField(max_length=30, verbose_name='Fecha'),
        ),
    ]
