# Generated by Django 4.2.11 on 2024-05-08 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0036_delete_agendamento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='semana',
            old_name='horario',
            new_name='horario2',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='horario',
            new_name='horario1',
        ),
    ]
