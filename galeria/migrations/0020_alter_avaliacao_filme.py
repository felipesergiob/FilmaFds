# Generated by Django 4.2 on 2023-05-12 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0019_alter_avaliacao_filme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='filme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliacoes', to='galeria.filme'),
        ),
    ]
