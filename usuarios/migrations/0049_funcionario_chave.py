# Generated by Django 4.2.11 on 2024-06-16 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0048_remove_funcionario_dupla_alter_funcionario_parceiro'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='chave',
            field=models.CharField(default='DEFAULT_KEY', max_length=100),
        ),
    ]