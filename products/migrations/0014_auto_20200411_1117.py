# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-11 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20200327_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=250),
        ),
    ]
