# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import Article.models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0032_auto_20150310_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='doc',
            field=models.FileField(default=False, help_text=b'Max Size 2.5MB', verbose_name=b'Attachment', upload_to=Article.models.get_upload_file_name),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='photo',
            field=models.FileField(default=b'himanshu.jpeg', help_text=b'Max Size 2.5MB', verbose_name=b'Attachment', upload_to=Article.models.get_upload_file_name),
            preserve_default=True,
        ),
    ]
