# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage
import Article.models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0007_auto_20150306_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.FileField(default=b'settings.MEDIA_ROOT/home/hitman/Documents/Django/post1/static/assests', storage=django.core.files.storage.FileSystemStorage(location=b'/static/assests'), upload_to=Article.models.get_upload_file_name),
            preserve_default=True,
        ),
    ]
