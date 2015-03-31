# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0006_auto_20150306_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location=b'/static/assests'), upload_to=b''),
            preserve_default=True,
        ),
    ]
