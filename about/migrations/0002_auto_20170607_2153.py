# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-07 21:53
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='content',
            field=tinymce.models.HTMLField(),
        ),
    ]
