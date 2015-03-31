# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0025_auto_20150308_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='photo',
            field=models.FileField(default=b'himanshu.jpeg', upload_to=b'/assets/%Y/%m/%d'),
            preserve_default=True,
        ),
    ]
