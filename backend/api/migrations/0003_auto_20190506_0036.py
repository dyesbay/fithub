# Generated by Django 2.0.13 on 2019-05-05 18:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='course',
            name='name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='event',
            name='title',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='lecture',
            name='course',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='api.Course'),
        ),
        migrations.AddField(
            model_name='lecture',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 6, 0, 36, 12, 637715)),
        ),
        migrations.AddField(
            model_name='lecture',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='lecture',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
