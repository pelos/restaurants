# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_vote', models.DateField(null=True, blank=True)),
                ('time_vote', models.TimeField(null=True, blank=True)),
                ('time_dish', models.TimeField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('adress', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='dish',
            name='restaurant',
            field=models.ForeignKey(to='polls.Restaurant'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='choice',
            name='dish',
            field=models.ForeignKey(blank=True, to='polls.Dish', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='choice',
            name='person',
            field=models.ForeignKey(to='polls.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='choice',
            name='rest_winner',
            field=models.ForeignKey(related_name=b'res_winner', blank=True, to='polls.Restaurant', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='choice',
            name='restaurant_vote',
            field=models.ForeignKey(related_name=b'res_vote', to='polls.Restaurant'),
            preserve_default=True,
        ),
    ]
