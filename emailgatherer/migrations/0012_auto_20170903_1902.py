# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 02:02
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('emailgatherer', '0011_join_ref_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='join',
            name='id',
        ),
        migrations.AlterField(
            model_name='join',
            name='ref_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
