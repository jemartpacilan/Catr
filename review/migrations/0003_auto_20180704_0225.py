# Generated by Django 2.0.6 on 2018-07-04 02:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_auto_20180704_0218'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='review_modified_at',
            new_name='review_date_modified',
        ),
    ]
