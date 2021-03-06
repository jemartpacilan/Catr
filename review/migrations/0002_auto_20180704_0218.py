# Generated by Django 2.0.6 on 2018-07-04 02:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review_modified_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 4, 2, 18, 24, 260842, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='review_date_submitted',
            field=models.DateTimeField(editable=False, verbose_name='date submitted'),
        ),
    ]
