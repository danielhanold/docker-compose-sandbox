# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 18:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0009_orderedperson'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='album',
            index_together=set([('media_type', 'num_stars')]),
        ),
    ]
