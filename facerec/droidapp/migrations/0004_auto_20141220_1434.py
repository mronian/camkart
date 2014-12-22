# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('droidapp', '0003_auto_20141220_1433'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='likes2',
            new_name='likes',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='views2',
            new_name='views',
        ),
    ]
