# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0012_auto_20150306_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.FileField(default=b'himanshu.jpeg', upload_to=b'documents/%Y/%m/%d'),
            preserve_default=True,
        ),
    ]
