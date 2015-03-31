# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0044_auto_20150318_1340'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('topic', models.CharField(max_length=50)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
