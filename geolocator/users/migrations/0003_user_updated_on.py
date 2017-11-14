# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_updated_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='updated_on',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
