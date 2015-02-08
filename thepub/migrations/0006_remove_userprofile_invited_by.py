# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thepub', '0005_auto_20150208_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='invited_by',
        ),
    ]
