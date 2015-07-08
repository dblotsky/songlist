# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setlist', '0007_featurerequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featurerequest',
            name='contact',
            field=models.CharField(help_text=b'Name, Email, or any other way I can know who you are.', max_length=255),
        ),
    ]
