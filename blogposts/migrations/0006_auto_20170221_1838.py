# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-21 12:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogposts', '0005_post_tagline'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='description',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='name',
            new_name='title',
        ),
    ]