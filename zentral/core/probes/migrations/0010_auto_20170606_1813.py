# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-06 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('probes', '0009_auto_20161212_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='path',
            field=models.FilePathField(blank=True, default=None, match='*.json', null=True, path='/zentral/feeds', recursive=True, unique=True),
        ),
        migrations.AlterField(
            model_name='feed',
            name='url',
            field=models.URLField(blank=True, default=None, null=True, unique=True),
        ),
    ]
