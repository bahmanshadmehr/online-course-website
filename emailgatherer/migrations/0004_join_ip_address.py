# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 01:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailgatherer', '0003_auto_20170903_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='ip_address',
            field=models.CharField(default=0, max_length=120),
            preserve_default=False,
        ),
    ]
