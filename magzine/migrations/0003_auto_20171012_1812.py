# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 12:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magzine', '0002_auto_20171012_1805'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Magzine',
            new_name='Mags',
        ),
    ]