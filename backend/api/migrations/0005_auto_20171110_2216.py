# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-10 22:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20171110_2034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bridgetable',
            old_name='direction_to_bid',
            new_name='direction_to_act',
        ),
    ]