# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('droidapp', '0002_auto_20141220_1426'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='likes',
            new_name='likes2',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='views',
            new_name='views2',
        ),
    ]
