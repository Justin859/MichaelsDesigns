# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-05-31 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('designs', '0006_auto_20170530_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='premier_brands',
            name='brand_logo',
            field=models.ImageField(max_length=255, null=True, upload_to=b'images/premier_brands/brand_logo'),
        ),
        migrations.AlterField(
            model_name='premier_brands',
            name='brand_main_photo',
            field=models.ImageField(max_length=255, null=True, upload_to=b'images/premier_brands/brand_main_photo'),
        ),
    ]
