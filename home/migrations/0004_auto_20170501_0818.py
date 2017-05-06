# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-01 08:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20170430_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='status',
            field=models.CharField(choices=[('looking for funds', 'looking for funds'), ('pledge succeeded', 'pledge succeeded'), ('pledge failed', 'pledge failed'), ('completed', 'completed')], default='looking for funds', max_length=40),
        ),
    ]