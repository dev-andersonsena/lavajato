# Generated by Django 4.2.11 on 2024-05-08 00:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0035_remove_agendamento_data_agendamento_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Agendamento',
        ),
    ]
