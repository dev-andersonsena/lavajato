# Generated by Django 4.2.11 on 2024-05-01 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0020_alter_userprofile_data_atual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='data_atual',
            field=models.DateField(blank=True, null=True),
        ),
    ]