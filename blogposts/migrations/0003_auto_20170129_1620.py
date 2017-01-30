# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-01-29 10:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogposts', '0002_remove_post_highlight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.Category'),
        ),
    ]