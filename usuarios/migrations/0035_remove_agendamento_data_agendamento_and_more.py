# Generated by Django 4.2.11 on 2024-05-08 00:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0034_remove_userprofile_data_agendamento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agendamento',
            name='data_agendamento',
        ),
        migrations.RemoveField(
            model_name='agendamento',
            name='horario',
        ),
        migrations.AddField(
            model_name='agendamento',
            name='data_hora_agendamento',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
