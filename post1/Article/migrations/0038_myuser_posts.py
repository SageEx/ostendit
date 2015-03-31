# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0037_auto_20150312_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='posts',
            field=models.IntegerField(default=10),
            preserve_default=True,
        ),
    ]
