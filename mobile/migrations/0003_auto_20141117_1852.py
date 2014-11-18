# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0002_auto_20141116_0152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telephone',
            name='copies',
        ),
        migrations.AddField(
            model_name='telephone',
            name='parent',
            field=models.ForeignKey(related_name='child', to='mobile.Telephone', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='telephone',
            name='original',
            field=models.ForeignKey(related_name='copies', to='mobile.Telephone', null=True),
            preserve_default=True,
        ),
    ]
