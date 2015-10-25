# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mklogin', '0002_auto_20151012_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='activationcode',
            field=models.IntegerField(max_length=6, default=1111111),
            preserve_default=False,
        ),
    ]
