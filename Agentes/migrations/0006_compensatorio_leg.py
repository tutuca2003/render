# Generated by Django 4.2.1 on 2024-08-26 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Agentes', '0005_compensatorio'),
    ]

    operations = [
        migrations.AddField(
            model_name='compensatorio',
            name='leg',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Agentes.agente'),
        ),
    ]
