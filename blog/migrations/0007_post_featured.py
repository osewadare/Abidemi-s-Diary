# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-11 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170511_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured',
            field=models.CharField(choices=[('Yes', 'yes'), ('No', 'No')], default='No', max_length=3),
        ),
    ]
