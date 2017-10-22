# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 10:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=100)),
                ('member_post', models.CharField(max_length=50)),
                ('member_image', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='bio',
            name='people',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.People'),
        ),
    ]
