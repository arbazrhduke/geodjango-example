# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('password', models.CharField(max_length=64)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address_line_1', models.CharField(max_length=200)),
                ('address_line_2', models.CharField(max_length=12)),
                ('landmark', models.CharField(max_length=32)),
                ('city', models.CharField(max_length=64)),
                ('state', models.CharField(max_length=64)),
                ('zip', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Address_Type',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True)),
                ('address', models.ForeignKey(to='users.Address')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='type',
            field=models.ForeignKey(to='users.Address_Type'),
        ),
        migrations.AddField(
            model_name='address',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
