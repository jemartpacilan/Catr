# Generated by Django 2.0.6 on 2018-07-03 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0009_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
