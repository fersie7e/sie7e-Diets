# Generated by Django 5.0 on 2023-12-23 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diets', '0011_alter_desayuno_platos_alter_desayuno_revision_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='alergias',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='habitos',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='observaciones',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='tratamientos',
            field=models.TextField(null=True),
        ),
    ]