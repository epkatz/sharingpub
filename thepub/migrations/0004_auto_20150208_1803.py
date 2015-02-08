# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thepub', '0003_auto_20150208_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shareable',
            name='deleted_datetime',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shareablelabel',
            name='deleted_datetime',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
