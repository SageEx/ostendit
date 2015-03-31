# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import Article.models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0027_auto_20150309_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='photo',
            field=models.FileField(default=b'himanshu.jpeg', upload_to=Article.models.get_upload_file_name),
            preserve_default=True,
        ),
    ]
