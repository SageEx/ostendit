# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0016_article_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='article',
            name='thumbnail1',
            field=models.FileField(default=b'himanshu.jpeg', upload_to=b'documents/%Y/%m/%d'),
            preserve_default=True,
        ),
    ]
