# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 19:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0005_auto_20170413_1422'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name_plural': 'people'},
        ),
        migrations.AddField(
            model_name='person',
            name='birthday',
            field=models.DateField(default=datetime.date.today, verbose_name='birthday'),
        ),
    ]
