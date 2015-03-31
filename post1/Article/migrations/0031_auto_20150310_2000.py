# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import Article.models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0030_auto_20150310_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='doc',
            field=models.FileField(default=None, help_text=b'Browse a File', verbose_name=b'Attachment', upload_to=Article.models.get_upload_file_name),
            preserve_default=True,
        ),
    ]
