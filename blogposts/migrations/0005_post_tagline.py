# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-21 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogposts', '0004_auto_20170221_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tagline',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]