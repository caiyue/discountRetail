# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-03 07:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discountRetailApp', '0005_auto_20171003_0710'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.CharField(default='\u6682\u65e0\u4fe1\u606f', max_length=100),
        ),
    ]