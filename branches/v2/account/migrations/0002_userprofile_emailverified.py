# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-14 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='emailverified',
            field=models.BooleanField(default=False),
        ),
    ]
