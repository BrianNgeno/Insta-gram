# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-05 07:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='images/')),
                ('Image_name', models.CharField(max_length=30)),
                ('Image_caption', models.TextField(max_length=40)),
                ('Likes', models.CharField(max_length=20)),
                ('Comments', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Profile_photo', models.ImageField(upload_to='images/')),
                ('Bio', models.TextField(max_length=50)),
            ],
        ),
    ]
