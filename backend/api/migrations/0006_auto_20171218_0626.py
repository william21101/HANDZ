# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-18 06:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20171218_0613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seats',
            old_name='table',
            new_name='bridgetable',
        ),
    ]
