# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-14 15:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0004_auto_20160914_1433'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'permissions': (('can_read', 'Can read'), ('can_comment', 'Can comment'))},
        ),
    ]