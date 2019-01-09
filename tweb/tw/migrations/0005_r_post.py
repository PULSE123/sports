# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-02 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tw', '0004_delete_imagegallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='r_Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('name', models.CharField(default=' ', max_length=200)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(null=True)),
                ('side', models.TextField(null=True)),
            ],
        ),
    ]
