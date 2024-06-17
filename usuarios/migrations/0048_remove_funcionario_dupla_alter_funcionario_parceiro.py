# Generated by Django 4.2.11 on 2024-06-16 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0047_remove_agendamento_dupla_registrada_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='dupla',
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='Parceiro',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dupla', to='usuarios.funcionario'),
        ),
    ]