# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20171114_0356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
