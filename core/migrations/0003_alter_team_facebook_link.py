# Generated by Django 4.2.4 on 2023-08-27 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_team_delete_teams'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='facebook_link',
            field=models.UUIDField(),
        ),
    ]
