# Generated by Django 5.0 on 2023-12-29 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diets', '0021_datos_revision_fecha_proxima_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datos_revision',
            name='almuerzo',
            field=models.JSONField(default=list, null=True),
        ),
        migrations.AlterField(
            model_name='datos_revision',
            name='cena',
            field=models.JSONField(default=list, null=True),
        ),
        migrations.AlterField(
            model_name='datos_revision',
            name='desayuno',
            field=models.JSONField(default=list, null=True),
        ),
        migrations.AlterField(
            model_name='datos_revision',
            name='media_manana',
            field=models.JSONField(default=list, null=True),
        ),
        migrations.AlterField(
            model_name='datos_revision',
            name='merienda',
            field=models.JSONField(default=list, null=True),
        ),
        migrations.AlterField(
            model_name='datos_revision',
            name='post_cena',
            field=models.JSONField(default=list, null=True),
        ),
    ]
