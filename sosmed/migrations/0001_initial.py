# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-22 20:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instagram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_depan', models.CharField(max_length=100)),
                ('nama_belakang', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
            ],
        ),
    ]
