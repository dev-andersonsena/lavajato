# Generated by Django 4.2.11 on 2024-04-22 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0010_delete_tipolavagem_userprofile_tipo_lavagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='dia',
            field=models.CharField(choices=[('segunda', 'Segunda-feira'), ('terca', 'Terça-feira'), ('quarta', 'Quarta-feira'), ('quinta', 'Quinta-feira'), ('sexta', 'Sexta-feira'), ('sabado', 'Sábado'), ('domingo', 'Domingo')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tipo_lavagem',
            field=models.CharField(choices=[('LAVAGEM_TECNICA', 'LAVAGEM TÉCNICA'), ('LIMPEZA_DETALHADA', 'LIMPEZA DETALHADA'), ('LIMPEZA DETALHADA + PROTECAO', 'LIMPEZA DETALHADA + PROTEÇÃO')], default='', max_length=100),
        ),
    ]