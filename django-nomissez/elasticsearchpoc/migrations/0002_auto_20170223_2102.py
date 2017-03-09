# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 21:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elasticsearchpoc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email_alias',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='thumbnail',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='title',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
