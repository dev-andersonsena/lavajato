# Generated by Django 4.2.11 on 2024-06-17 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0052_alter_agendamento_options_alter_funcionario_chave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='chave',
            field=models.CharField(max_length=100),
        ),
    ]
