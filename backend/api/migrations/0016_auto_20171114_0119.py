# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 01:19
from __future__ import unicode_literals

import api.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20171114_0118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bridgetable',
            name='trick',
            field=api.models.TrickField(default=None, null=True),
        ),
    ]
