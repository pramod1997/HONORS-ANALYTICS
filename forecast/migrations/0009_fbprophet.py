# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-30 17:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forecast', '0008_croston'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fbprophet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='Fbprophet/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]