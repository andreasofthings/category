# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-21 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='Category',
            name="name",
            field=models.CharField(help_text=b'Short descriptive name for this category.', max_length=200, unique=True)),
    ]
