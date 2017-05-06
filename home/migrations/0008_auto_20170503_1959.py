# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_creditcards'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditcards',
            name='cnum',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='creditcards',
            name='exp_date',
            field=models.DateField(null=True),
        ),
    ]