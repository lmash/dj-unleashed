# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-10 20:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=63)),
                ('slug', models.SlugField(help_text='A label for URL config.', max_length=63, unique_for_month='pub_date')),
                ('text', models.TextField()),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='date published')),
                ('startup', models.ManyToManyField(related_name='blog_posts', to='organizer.Startup')),
                ('tag', models.ManyToManyField(related_name='blog_posts', to='organizer.Tag')),
            ],
            options={
                'ordering': ['-pub_date', 'title'],
                'verbose_name': 'blog post',
                'get_latest_by': 'pub_date',
            },
        ),
    ]
