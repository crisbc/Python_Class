# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfiles', '0004_auto_20171204_0210'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='partner_location_preference',
            field=models.CharField(default='Any', max_length=250),
        ),
    ]