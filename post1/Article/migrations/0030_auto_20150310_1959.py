# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import Article.models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0029_article_doc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='doc',
            field=models.FileField(default=b'', help_text=b'Browse a File', verbose_name=b'Attachment', upload_to=Article.models.get_upload_file_name),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='photo',
            field=models.FileField(default=b'himanshu.jpeg', help_text=b'Browse a File', verbose_name=b'Attachment', upload_to=Article.models.get_upload_file_name),
            preserve_default=True,
        ),
    ]
