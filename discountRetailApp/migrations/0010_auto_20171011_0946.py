# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-11 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discountRetailApp', '0009_auto_20171011_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.CharField(default='no info', max_length=30),
        ),
    ]
