# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-10-15 02:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discountRetailApp', '0013_auto_20171012_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoryinfo',
            name='categoryId',
        ),
        migrations.RemoveField(
            model_name='consumerinfo',
            name='consumerid',
        ),
        migrations.RemoveField(
            model_name='sellerinfo',
            name='sellerid',
        ),
        migrations.RemoveField(
            model_name='waresinfo',
            name='wareId',
        ),
    ]
