# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0026_auto_20150309_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='photo',
            field=models.FileField(default=b'himanshu.jpeg', upload_to=b'/assets'),
            preserve_default=True,
        ),
    ]
