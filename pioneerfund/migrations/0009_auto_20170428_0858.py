# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 08:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pioneerfund', '0008_auto_20170428_0802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
