# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import Article.models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0010_auto_20150306_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.FileField(default=b'himanshu.jpeg', upload_to=Article.models.get_upload_file_name),
            preserve_default=True,
        ),
    ]
