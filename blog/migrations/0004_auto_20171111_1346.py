# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-11 04:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20171111_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Python', 'Python'), ('Django', 'Django'), ('Etc', 'Etc')], default='Dj', max_length=6, verbose_name='Category'),
        ),
    ]
