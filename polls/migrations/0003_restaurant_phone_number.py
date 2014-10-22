# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20141018_0009'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='phone_number',
            field=models.CharField(max_length=12, null=True, blank=True),
            preserve_default=True,
        ),
    ]
