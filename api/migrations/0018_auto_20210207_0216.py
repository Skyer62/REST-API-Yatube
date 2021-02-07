# Generated by Django 3.1.6 on 2021-02-06 21:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0017_group_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follow',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='asdsad', to=settings.AUTH_USER_MODEL, verbose_name='Подписчик'),
        ),
    ]