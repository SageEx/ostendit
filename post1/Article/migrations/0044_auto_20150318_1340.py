# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0043_auto_20150318_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='security_answer',
            field=models.CharField(default=b'yes', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='security_question',
            field=models.CharField(default=b'what', max_length=50),
            preserve_default=True,
        ),
    ]
