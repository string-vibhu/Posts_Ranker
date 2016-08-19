# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-18 10:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranking_algo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Features', models.CharField(max_length=20)),
                ('Weight', models.FloatField(default=0, null=True)),
            ],
        ),
    ]