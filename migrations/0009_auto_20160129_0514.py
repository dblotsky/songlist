# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlist', '0008_auto_20150708_0445'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='played',
            new_name='on_list',
        ),
    ]
