# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-19 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GenreMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(db_index=True, max_length=127, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MovieData',
            fields=[
                ('movie_id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('name', models.TextField(db_index=True)),
                ('director', models.CharField(max_length=247)),
                ('imdb_score', models.FloatField(default=None)),
                ('popularity', models.FloatField(default=None)),
                ('genre', models.ManyToManyField(related_name='movies', related_query_name='movie', to='movie_app.GenreMeta')),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
    ]