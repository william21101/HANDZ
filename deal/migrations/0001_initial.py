# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 20:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BridgeTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardinal_direction', models.IntegerField()),
                ('suit', models.CharField(max_length=7)),
                ('value', models.CharField(max_length=7)),
                ('card_position', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('deal_id', models.AutoField(primary_key=True, serialize=False)),
                ('hand_string', models.CharField(max_length=52)),
                ('dealer', models.IntegerField()),
                ('vulnerability', models.IntegerField()),
                ('board_number', models.IntegerField()),
                ('bridge_table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='deal.BridgeTable')),
            ],
        ),
        migrations.CreateModel(
            name='Trick',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leading_suit', models.CharField(blank=True, max_length=7)),
                ('deal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='deal.Deal')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hand_position', models.IntegerField(default=-1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='deal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='deal.Deal'),
        ),
        migrations.AddField(
            model_name='card',
            name='trick',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='deal.Trick'),
        ),
    ]
