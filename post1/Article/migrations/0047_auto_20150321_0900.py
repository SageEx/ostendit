# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0046_article_topic'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Topics',
        ),
        migrations.RemoveField(
            model_name='article',
            name='topic',
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(default=b'himanshu', max_length=50),
            preserve_default=True,
        ),
    ]
