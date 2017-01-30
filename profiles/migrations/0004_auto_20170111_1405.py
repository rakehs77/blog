# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-11 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20170111_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField(default='Write something about website.', max_length=5000)),
            ],
        ),
        migrations.DeleteModel(
            name='About',
        ),
        migrations.AlterField(
            model_name='heading',
            name='pagename',
            field=models.CharField(editable=False, max_length=32),
        ),
    ]
