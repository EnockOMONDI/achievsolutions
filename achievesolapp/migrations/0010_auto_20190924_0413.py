# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-09-24 01:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('achievesolapp', '0009_auto_20190924_0412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='name',
            new_name='blog_name',
        ),
    ]
