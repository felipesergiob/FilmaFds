# Generated by Django 4.2 on 2023-05-10 18:15

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0013_rename_comment_comment_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='filme',
            name='estrelas',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
    ]
