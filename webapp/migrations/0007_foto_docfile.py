# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-29 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='foto',
            name='docfile',
            field=models.FileField(blank=True, upload_to=b'documents/%Y/%m/%d'),
        ),
    ]