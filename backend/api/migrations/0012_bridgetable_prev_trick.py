# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-11 20:31
from __future__ import unicode_literals

import api.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_bridgetable_phase'),
    ]

    operations = [
        migrations.AddField(
            model_name='bridgetable',
            name='prev_trick',
            field=api.models.TrickField(default=''),
        ),
    ]