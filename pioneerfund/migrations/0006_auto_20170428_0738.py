# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 07:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pioneerfund', '0005_customeruser'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomerUser',
            new_name='CustomUser',
        ),
    ]