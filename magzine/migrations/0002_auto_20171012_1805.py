# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 12:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magzine', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bio',
            new_name='Pages',
        ),
    ]
