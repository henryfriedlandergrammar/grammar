# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-28 12:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sentenceGen', '0008_auto_20160828_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='chosen_words',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='question',
            name='correct_words',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]