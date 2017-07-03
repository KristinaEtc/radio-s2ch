# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('author', models.CharField(max_length=64)),
                ('comment', models.CharField(max_length=255)),
                ('content', models.FileField(upload_to='')),
                ('status', models.CharField(choices=[('i', 'Initiating'), ('p', 'Processing'), ('r', 'Ready'), ('e', 'Error')], default='i', max_length=1)),
                ('source', models.CharField(choices=[('y', 'Youtube'), ('f', 'User file')], max_length=1)),
                ('source_id', models.CharField(default=None, max_length=255, null=True)),
                ('votes_up', models.IntegerField(default=0)),
                ('votes_down', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
