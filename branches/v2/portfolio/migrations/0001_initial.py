# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-13 10:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='portFolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('subtitle', models.CharField(max_length=200)),
                ('uuid', models.CharField(default='DUMMY', max_length=200)),
                ('desc', models.CharField(max_length=4000)),
                ('deleted', models.BooleanField(default=False)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('lastupdate_date', models.DateTimeField(auto_now_add=True)),
                ('public', models.BooleanField(default=False)),
                ('snapshot', models.FileField(upload_to='portfolios')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='portfolioItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectname', models.CharField(max_length=200)),
                ('startdate', models.DateTimeField()),
                ('enddate', models.DateTimeField()),
                ('desc', models.CharField(max_length=1000)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('lastupdate_date', models.DateTimeField(auto_now_add=True)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.portFolio')),
            ],
        ),
        migrations.CreateModel(
            name='portfolioItemMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mediapath', models.FileField(upload_to='portfoliomedia')),
                ('mediatype', models.CharField(max_length=100)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('lastupdate_date', models.DateTimeField(auto_now_add=True)),
                ('portfolioitem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.portfolioItem')),
            ],
        ),
        migrations.CreateModel(
            name='relProjectPortfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.portFolio')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
        ),
    ]
