# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-09 00:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0003_auto_20171109_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default=''),
        ),
    ]
