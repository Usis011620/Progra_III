# Generated by Django 3.2.9 on 2021-12-11 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistemaclinica', '0006_alter_citas_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recetas',
            name='fecha',
            field=models.DateField(max_length=10, verbose_name='fecha'),
        ),
    ]
