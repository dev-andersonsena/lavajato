# Generated by Django 4.2.11 on 2024-04-09 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_alter_userprofile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='telefone',
        ),
    ]
