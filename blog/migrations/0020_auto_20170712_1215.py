# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-12 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20170712_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogsettings',
            name='description',
            field=models.CharField(max_length=250, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='blogsettings',
            name='email',
            field=models.CharField(max_length=25, verbose_name='Admin Email'),
        ),
        migrations.AlterField(
            model_name='blogsettings',
            name='facebook_id',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='blogsettings',
            name='instagram_id',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='blogsettings',
            name='linkedin_id',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='blogsettings',
            name='tagline',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='blogsettings',
            name='title',
            field=models.CharField(max_length=20, verbose_name='Blog Title'),
        ),
        migrations.AlterField(
            model_name='blogsettings',
            name='twitter_id',
            field=models.CharField(max_length=50),
        ),
    ]
