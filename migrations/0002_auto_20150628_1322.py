# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': ('artist',)},
        ),
        migrations.AlterField(
            model_name='link',
            name='song',
            field=models.ForeignKey(related_name='links', to='setlist.Song'),
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.ForeignKey(related_name='songs', to='setlist.Artist'),
        ),
    ]
