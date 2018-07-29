# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-05-03 22:04
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce_4.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelFoo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', tinymce_4.fields.TinyMCEModelField(verbose_name='Foo content')),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=tinymce_4.fields.TinyMCEModelField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=tinymce_4.fields.TinyMCEModelField(),
        ),
    ]