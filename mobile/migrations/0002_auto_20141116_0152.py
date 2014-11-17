# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mobile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile',
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(related_name='profile', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='telephone',
            name='copies',
            field=models.CommaSeparatedIntegerField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='telephone',
            name='original',
            field=models.PositiveSmallIntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='telephone',
            name='owner',
            field=models.ForeignKey(related_name='telephone', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='telephone',
            name='sound_url',
            field=models.URLField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='telephone',
            name='text',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
