# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 07:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170430_0626'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='country',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='state',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
