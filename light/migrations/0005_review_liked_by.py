# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-07 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('light', '0004_review_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='liked_by',
            field=models.ManyToManyField(related_name='likes', to='light.User'),
        ),
    ]
