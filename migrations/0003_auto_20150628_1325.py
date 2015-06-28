# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlist', '0002_auto_20150628_1322'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': ('artist__name',)},
        ),
        migrations.AddField(
            model_name='song',
            name='played',
            field=models.BooleanField(default=False),
        ),
    ]
