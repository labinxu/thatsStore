# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 14:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xstores', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='xgoods',
            old_name='xstores',
            new_name='xstore',
        ),
    ]
