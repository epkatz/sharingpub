# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label_name', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Shareable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('deleted_datetime', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ShareableLabel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('deleted_datetime', models.DateTimeField()),
                ('label', models.ForeignKey(to='thepub.Label')),
                ('shareable', models.ForeignKey(to='thepub.Shareable')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(unique=True, max_length=2000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_test_user', models.BooleanField(default=False)),
                ('invited_by', models.ForeignKey(to='thepub.UserProfile')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='shareable',
            name='labels',
            field=models.ManyToManyField(to='thepub.Label', through='thepub.ShareableLabel'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shareable',
            name='shared_by',
            field=models.ForeignKey(to='thepub.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='shareable',
            name='url',
            field=models.ForeignKey(to='thepub.Url'),
            preserve_default=True,
        ),
    ]
