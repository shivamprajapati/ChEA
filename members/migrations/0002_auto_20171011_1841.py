# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 13:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bio',
            old_name='people',
            new_name='member',
        ),
        migrations.AlterField(
            model_name='people',
            name='member_image',
            field=models.FileField(upload_to=''),
        ),
    ]
