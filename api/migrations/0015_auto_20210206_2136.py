# Generated by Django 3.1.6 on 2021-02-06 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20210206_2134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='user',
            new_name='username',
        ),
    ]
