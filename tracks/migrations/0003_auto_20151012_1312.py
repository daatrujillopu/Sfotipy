# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0002_auto_20151012_1306'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tracks',
            new_name='Track',
        ),
    ]
