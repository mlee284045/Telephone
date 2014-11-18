# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0005_auto_20141118_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telephone',
            name='original',
            field=models.ForeignKey(related_name='copies', blank=True, to='mobile.Telephone', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='telephone',
            name='parent',
            field=models.ForeignKey(related_name='child', blank=True, to='mobile.Telephone', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='telephone',
            name='sound_url',
            field=models.URLField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
