# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 15:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description',
            field=models.CharField(default='no description', max_length=520),
            preserve_default=False,
        ),
    ]
