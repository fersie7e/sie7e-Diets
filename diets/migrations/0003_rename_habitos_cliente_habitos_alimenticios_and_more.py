# Generated by Django 5.0 on 2023-12-22 18:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diets', '0002_rename_transito_intestinal_client_transito_intestinal_normal_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Client',
            new_name='Cliente',
        ),
        
    ]