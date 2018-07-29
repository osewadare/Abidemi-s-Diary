# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-13 20:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0022_auto_20170712_1302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='setting',
            name='site_url',
            field=models.CharField(default='http://www.site.com', max_length=50, verbose_name='Site URL'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='tagline',
            field=models.CharField(max_length=25, verbose_name='Tagline'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='title',
            field=models.CharField(max_length=20, verbose_name='Site Title'),
        ),
    ]