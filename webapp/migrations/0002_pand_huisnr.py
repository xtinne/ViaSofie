# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-19 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pand',
            name='huisnr',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
