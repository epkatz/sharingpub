# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thepub', '0002_userprofile_is_beta_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shareable',
            name='url',
            field=models.URLField(unique=True, max_length=2000),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='Url',
        ),
    ]
