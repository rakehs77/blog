# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-21 06:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogposts', '0003_auto_20170129_1620'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on']},
        ),
    ]
