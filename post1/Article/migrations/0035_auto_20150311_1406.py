# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import Article.models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0034_auto_20150311_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='photo',
            field=models.FileField(upload_to=Article.models.get_upload_file_name, null=True, verbose_name=b'Attachment', blank=True),
            preserve_default=True,
        ),
    ]
