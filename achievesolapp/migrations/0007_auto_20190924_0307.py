# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-09-24 00:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('achievesolapp', '0006_blog_available'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ('-created_at',)},
        ),
    ]
