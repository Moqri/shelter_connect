# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-26 00:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserve', '0002_auto_20160525_2231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='date',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='shelter',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='user',
        ),
        migrations.AddField(
            model_name='reservation',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='shelter',
            name='beds_available',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='shelter',
            name='beds_total',
            field=models.IntegerField(default=0),
        ),
    ]