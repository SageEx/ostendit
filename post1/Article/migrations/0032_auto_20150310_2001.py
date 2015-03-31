# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import Article.models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0031_auto_20150310_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='doc',
            field=models.FileField(default=False, help_text=b'Browse a File', verbose_name=b'Attachment', upload_to=Article.models.get_upload_file_name),
            preserve_default=True,
        ),
    ]
