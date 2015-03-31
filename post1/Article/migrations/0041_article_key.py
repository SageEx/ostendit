# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0040_auto_20150317_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='key',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
