# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-02 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default='email', max_length=254),
        ),
    ]
