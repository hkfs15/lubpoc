# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lub', '0003_auto_20151015_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lub',
            name='builderapproval',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='lub',
            name='density',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='lub',
            name='flashpoint',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='lub',
            name='sulfated_ash',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='lub',
            name='totalbase',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='lub',
            name='viscosity_100',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='lub',
            name='viscosity_40',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='lub',
            name='viscosity_index',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='lub',
            name='wt',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
