# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-14 23:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement_box_monitor', '0002_auto_20160609_1759'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeasurementBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=256)),
                ('hardware', models.CharField(max_length=256)),
                ('software', models.CharField(max_length=256)),
                ('connection_type', models.CharField(max_length=256)),
                ('notes', models.CharField(max_length=1024)),
            ],
        ),
    ]
