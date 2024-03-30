# Generated by Django 5.0 on 2023-12-23 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diets', '0007_rename_cliente_analitica_analitica_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comida',
            name='categoria_comida',
        ),
        migrations.AddField(
            model_name='comida',
            name='categorias_comida',
            field=models.ManyToManyField(blank=True, related_name='categorias_comida', to='diets.categoria_comida'),
        ),
    ]
