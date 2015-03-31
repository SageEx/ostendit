# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import Article.models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0004_auto_20150305_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumbnail',
            field=models.FileField(default=b'settings.MEDIA_ROOT', upload_to=Article.models.get_upload_file_name),
            preserve_default=True,
        ),
    ]
