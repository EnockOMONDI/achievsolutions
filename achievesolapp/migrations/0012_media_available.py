# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-09-24 04:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achievesolapp', '0011_auto_20190924_0515'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
