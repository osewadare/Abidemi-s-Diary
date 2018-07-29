# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-12 12:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20170712_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='blog.Category'),
        ),
    ]
