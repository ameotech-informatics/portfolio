# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-14 12:20
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20160913_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 14, 17, 50, 57, 722000)),
        ),
        migrations.AddField(
            model_name='project',
            name='lastupdate_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 14, 17, 50, 57, 722000)),
        ),
    ]
