# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 02:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emailgatherer', '0012_auto_20170903_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='join',
            name='ref_id',
            field=models.CharField(default='', max_length=120),
        ),
    ]