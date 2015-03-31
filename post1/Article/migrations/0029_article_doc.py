# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import Article.models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0028_auto_20150309_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='doc',
            field=models.FileField(default=b'', upload_to=Article.models.get_upload_file_name),
            preserve_default=True,
        ),
    ]
