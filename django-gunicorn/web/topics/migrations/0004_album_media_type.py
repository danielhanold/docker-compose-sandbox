# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-13 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0003_person_shirt_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='media_type',
            field=models.CharField(choices=[('Audio', (('vinyl', 'Vinyl'), ('cd', 'CD'))), ('Video', (('vhs', 'VHS Tape'), ('dvd', 'DVD'))), (None, 'Unknown')], default='cd', max_length=10),
        ),
    ]
