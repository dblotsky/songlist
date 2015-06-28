# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlist', '0005_auto_20150628_1407'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ('name',)},
        ),
    ]
