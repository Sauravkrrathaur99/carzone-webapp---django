# Generated by Django 3.2 on 2022-04-15 16:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_rename_teams_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='last',
            new_name='last_name',
        ),
    ]