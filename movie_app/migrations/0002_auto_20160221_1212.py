# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviedata',
            name='name',
            field=models.TextField(db_index=True, unique=True),
        ),
    ]
