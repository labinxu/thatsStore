# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xstores', '0002_auto_20161121_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='xgoods',
            name='slug',
            field=models.CharField(max_length=256, unique=True, verbose_name='网址'),
        ),
    ]
