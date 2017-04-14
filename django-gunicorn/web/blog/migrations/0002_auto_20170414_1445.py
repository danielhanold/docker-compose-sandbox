# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-14 18:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='mod_date',
            field=models.DateField(verbose_name=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='entry',
            name='n_comments',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='entry',
            name='n_pingbacks',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='entry',
            name='pub_date',
            field=models.DateField(verbose_name=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='entry',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]