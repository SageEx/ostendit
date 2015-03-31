# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0041_article_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='security_answer',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myuser',
            name='security_question',
            field=models.CharField(default=b"What is your father's name", max_length=50),
            preserve_default=True,
        ),
    ]
