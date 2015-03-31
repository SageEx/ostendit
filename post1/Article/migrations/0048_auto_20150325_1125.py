# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0047_auto_20150321_0900'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='user_permission',
            field=models.IntegerField(default=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='security_question',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
