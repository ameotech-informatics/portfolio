# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-15 09:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20160915_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 15, 15, 17, 43, 501000)),
        ),
        migrations.AlterField(
            model_name='project',
            name='lastupdate_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 15, 15, 17, 43, 501000)),
        ),
    ]