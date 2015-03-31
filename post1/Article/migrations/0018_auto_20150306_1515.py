# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0017_auto_20150306_1503'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='thumbnail1',
        ),
        migrations.AddField(
            model_name='article',
            name='photo',
            field=models.ImageField(default=b'himanshu.jpeg', upload_to=b'documents/%Y/%m/%d'),
            preserve_default=True,
        ),
    ]
