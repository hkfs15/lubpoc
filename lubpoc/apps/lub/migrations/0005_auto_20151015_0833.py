# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lub', '0004_auto_20151015_0411'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='lub_type',
            field=models.CharField(max_length=50, blank=True, choices=[('ADVANCED', '高级润滑油'), ('NORMAL', '普通润滑油')]),
        ),
        migrations.AddField(
            model_name='car',
            name='motor_type',
            field=models.CharField(max_length=50, blank=True, choices=[('CHAIYOU', '柴油发动机'), ('QIYOU', '汽油发动机')]),
        ),
        migrations.AlterField(
            model_name='engine',
            name='spec',
            field=models.TextField(blank=True),
        ),
    ]
