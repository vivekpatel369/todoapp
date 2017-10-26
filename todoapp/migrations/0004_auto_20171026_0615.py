# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_auto_20171026_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todos',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
