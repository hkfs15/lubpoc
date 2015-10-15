# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lub', '0002_auto_20151015_0406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lub',
            name='lub_type',
            field=models.CharField(choices=[('ADVANCED', '高级润滑油'), ('NORMAL', '普通润滑油')], max_length=50),
        ),
        migrations.AlterField(
            model_name='lub',
            name='motor_type',
            field=models.CharField(choices=[('CHAIYOU', '柴油发动机'), ('QIYOU', '汽油发动机')], max_length=50),
        ),
    ]
