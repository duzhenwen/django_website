# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-04 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_infor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('telephone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
