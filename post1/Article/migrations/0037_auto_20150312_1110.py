# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import Article.models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0036_article_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('user_name', models.CharField(max_length=200)),
                ('user_password', models.CharField(max_length=50)),
                ('user_email', models.CharField(default=b'', max_length=200)),
                ('user_college', models.CharField(default=b'', max_length=50)),
                ('photo', models.FileField(default=b'index.jpeg', upload_to=Article.models.get_upload_file_name)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(default=b'pingu', max_length=50),
            preserve_default=True,
        ),
    ]
