# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0015_remove_article_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumbnail',
            field=models.FileField(default=b'himanshu.jpeg', upload_to=b'documents/%Y/%m/%d'),
            preserve_default=True,
        ),
    ]
