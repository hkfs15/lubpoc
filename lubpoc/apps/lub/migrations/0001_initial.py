# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('year', models.IntegerField()),
                ('model', models.CharField(max_length=128)),
                ('spec', models.FilePathField(recursive=True, match='car_manual_*', path='static/manual/')),
                ('last_modified', models.DateField(verbose_name='Last modified', auto_now=True)),
                ('slug', models.SlugField(verbose_name='Car slug', unique=True)),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('brand', models.CharField(max_length=128)),
                ('model', models.CharField(max_length=128)),
                ('spec', models.TextField()),
                ('last_modified', models.DateField(verbose_name='Last modified', auto_now=True)),
                ('slug', models.SlugField(verbose_name='Engine slug', unique=True)),
            ],
            options={
                'verbose_name': 'Engine',
                'verbose_name_plural': 'Engines',
            },
        ),
        migrations.CreateModel(
            name='Lub',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Lub name', max_length=128)),
                ('datasheet', models.TextField(verbose_name='Lub datasheet', blank=True)),
                ('lub_type', models.TextField(choices=[('ADVANCED', '高级润滑油'), ('NORMAL', '普通润滑油')])),
                ('motor_type', models.TextField(choices=[('CHAIYOU', '柴油发动机'), ('QIYOU', '汽油发动机')])),
                ('specifications', models.TextField(blank=True)),
                ('builderapproval', models.CharField(max_length=128)),
                ('sae_grade', models.CharField(choices=[('S1', 'S1'), ('S2', 'S2'), ('S3', 'S3'), ('S4', 'S4'), ('S5', 'S5'), ('S6', 'S6'), ('S7', 'S7')], max_length=50)),
                ('density', models.CharField(max_length=128)),
                ('viscosity_40', models.CharField(max_length=128)),
                ('viscosity_100', models.CharField(max_length=128)),
                ('viscosity_index', models.CharField(max_length=128)),
                ('sulfated_ash', models.CharField(max_length=128)),
                ('wt', models.CharField(max_length=128)),
                ('totalbase', models.CharField(max_length=128)),
                ('flashpoint', models.CharField(max_length=128)),
                ('pourpoint', models.CharField(max_length=128)),
                ('last_modified', models.DateField(verbose_name='Last modified', auto_now=True)),
                ('slug', models.SlugField(verbose_name='Lub slug', unique=True)),
            ],
            options={
                'verbose_name': 'Lub',
                'verbose_name_plural': 'Lubs',
            },
        ),
        migrations.CreateModel(
            name='LubMake',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Lubricator maker', max_length=128)),
                ('website', models.URLField(verbose_name='Lubricator maker offical website', blank=True)),
                ('description', models.TextField(verbose_name='Lub description', blank=True)),
                ('last_modified', models.DateField(verbose_name='Last modified', auto_now=True)),
                ('slug', models.SlugField(verbose_name='LubMaker slug', unique=True)),
            ],
            options={
                'verbose_name': 'LubMake',
                'verbose_name_plural': 'LubMakes',
            },
        ),
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Make name', max_length=40)),
                ('website', models.URLField(verbose_name='Make offical website', blank=True)),
                ('description', models.TextField(verbose_name='Make description', blank=True)),
                ('last_modified', models.DateField(verbose_name='Last modified', auto_now=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'Make',
                'verbose_name_plural': 'Makes',
            },
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Series name', max_length=128)),
                ('last_modified', models.DateField(verbose_name='Last modified', auto_now=True)),
                ('slug', models.SlugField(unique=True)),
                ('make', models.ForeignKey(to='lub.Make')),
            ],
            options={
                'verbose_name': 'Series',
                'verbose_name_plural': 'Series',
            },
        ),
        migrations.AddField(
            model_name='lub',
            name='lubmake',
            field=models.ForeignKey(to='lub.LubMake'),
        ),
        migrations.AddField(
            model_name='engine',
            name='series',
            field=models.OneToOneField(to='lub.Series'),
        ),
        migrations.AddField(
            model_name='car',
            name='manual_listed_lubs',
            field=models.ManyToManyField(to='lub.Lub'),
        ),
        migrations.AddField(
            model_name='car',
            name='series',
            field=models.ForeignKey(to='lub.Series'),
        ),
    ]
