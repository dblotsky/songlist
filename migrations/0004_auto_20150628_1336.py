# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlist', '0003_auto_20150628_1325'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artist',
            options={'ordering': ('name',)},
        ),
        migrations.AlterField(
            model_name='link',
            name='song',
            field=models.ForeignKey(related_name='links', to='setlist.Song', null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.ForeignKey(related_name='songs', to='setlist.Artist', null=True),
        ),
        migrations.AlterUniqueTogether(
            name='link',
            unique_together=set([('song', 'url')]),
        ),
        migrations.AlterUniqueTogether(
            name='song',
            unique_together=set([('name', 'artist')]),
        ),
    ]
