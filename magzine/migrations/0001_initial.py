# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 12:35
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
                ('page_title', models.CharField(max_length=100)),
                ('pages', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Magzine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('magzine_name', models.CharField(max_length=100)),
                ('magzine_year', models.CharField(max_length=10)),
                ('magzine_coverpage', models.FileField(upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='bio',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magzine.Magzine'),
        ),
    ]
