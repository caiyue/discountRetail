# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-03 08:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discountRetailApp', '0006_person_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='update_time',
            field=models.CharField(default='\u7a7a\u95f4', max_length=256, verbose_name='\u66f4\u65b0\u65f6\u95f4'),
        ),
    ]
