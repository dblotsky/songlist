# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlist', '0006_auto_20150628_1450'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('suggestion', models.TextField()),
                ('contact', models.TextField(help_text=b'Name, Email, or any other way I can know who you are.')),
            ],
        ),
    ]
