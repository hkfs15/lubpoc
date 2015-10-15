# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lub', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='manual_listed_lubs',
            field=models.ManyToManyField(to='lub.Lub', blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='spec',
            field=models.FilePathField(path='static/manual/', recursive=True, match='car_manual_*', blank=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='year',
            field=models.IntegerField(blank=True),
        ),
    ]
