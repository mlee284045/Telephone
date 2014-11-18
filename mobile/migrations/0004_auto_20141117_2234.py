# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0003_auto_20141117_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telephone',
            name='owner',
            field=models.ForeignKey(related_name='telephones', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
