# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mklogin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='kategoria',
        ),
        migrations.AddField(
            model_name='myuser',
            name='kategoria',
            field=models.ManyToManyField(to='mklogin.Kategoria', blank=True, null=True),
        ),
    ]
