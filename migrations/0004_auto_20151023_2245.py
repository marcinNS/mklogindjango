# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mklogin', '0003_myuser_activationcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='activationcode',
            field=models.IntegerField(),
        ),
    ]
