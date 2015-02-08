# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thepub', '0004_auto_20150208_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='invited_by',
            field=models.ForeignKey(to='thepub.UserProfile', null=True),
            preserve_default=True,
        ),
    ]
