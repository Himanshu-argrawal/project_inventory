# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-14 04:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20170213_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]