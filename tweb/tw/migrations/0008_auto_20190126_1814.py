# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-01-26 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tw', '0007_achpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marquee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='achpost',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='achpost',
            name='name',
            field=models.CharField(default=' ', max_length=200),
        ),
    ]
