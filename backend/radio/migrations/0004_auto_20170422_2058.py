# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0003_auto_20170422_1935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='content',
        ),
        migrations.AddField(
            model_name='track',
            name='filename',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
