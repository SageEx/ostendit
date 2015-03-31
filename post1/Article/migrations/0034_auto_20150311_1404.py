# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import Article.models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0033_auto_20150310_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='doc',
            field=models.FileField(upload_to=Article.models.get_upload_file_name, null=True, verbose_name=b'Attachment', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='photo',
            field=models.FileField(default=b'himanshu.jpeg', upload_to=Article.models.get_upload_file_name, verbose_name=b'Attachment'),
            preserve_default=True,
        ),
    ]
