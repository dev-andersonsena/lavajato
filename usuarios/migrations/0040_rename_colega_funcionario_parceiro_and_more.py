# Generated by Django 4.2.11 on 2024-05-30 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0039_userprofile_lavagem_adicional'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funcionario',
            old_name='colega',
            new_name='Parceiro',
        ),
        migrations.RenameField(
            model_name='funcionario',
            old_name='Dupla',
            new_name='dupla',
        ),
    ]
