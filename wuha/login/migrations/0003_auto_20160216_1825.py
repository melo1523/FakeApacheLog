# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-16 18:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20160216_0330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filelist',
            name='username',
        ),
        migrations.DeleteModel(
            name='filelist',
        ),
        migrations.DeleteModel(
            name='namepw',
        ),
    ]