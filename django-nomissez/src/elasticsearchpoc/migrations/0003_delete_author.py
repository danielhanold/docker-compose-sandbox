# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-08 16:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elasticsearchpoc', '0002_auto_20170223_2102'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
    ]
