# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thepub', '0006_remove_userprofile_invited_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shareable',
            name='deleted_datetime',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shareable',
            name='url',
            field=models.URLField(max_length=2000),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='shareablelabel',
            name='deleted_datetime',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
