# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-11 09:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discountRetailApp', '0007_blog_update_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='update_time',
            field=models.CharField(default='\u6682\u65e0\u66f4\u65b0', max_length=256, verbose_name='\u66f4\u65b0\u65f6\u95f4'),
        ),
    ]