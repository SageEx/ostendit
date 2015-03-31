# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0035_auto_20150311_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.CharField(help_text=b'Max. Characters = 30', max_length=30, null=True, blank=True),
            preserve_default=True,
        ),
    ]
