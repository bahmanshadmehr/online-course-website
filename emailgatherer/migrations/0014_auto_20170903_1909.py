# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 02:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emailgatherer', '0013_auto_20170903_1905'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='join',
            unique_together=set([('email', 'ref_id')]),
        ),
    ]
