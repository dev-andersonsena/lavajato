# Generated by Django 4.2.11 on 2024-05-03 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0032_alter_userprofile_data_agendamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='data_agendamento',
            field=models.DateField(),
        ),
    ]
