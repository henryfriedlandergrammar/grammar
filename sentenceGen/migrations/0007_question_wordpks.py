# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-28 03:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentenceGen', '0006_auto_20160828_0233'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='wordPKs',
            field=models.CharField(default=' ', max_length=2000),
            preserve_default=False,
        ),
    ]
