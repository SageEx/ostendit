# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import Article.models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0042_auto_20150317_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='photo',
            field=models.FileField(default=b'himanshu.jpeg', upload_to=Article.models.get_upload_file_name),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='security_answer',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='security_question',
            field=models.CharField(max_length=50),
            preserve_default=True,
        ),
    ]
