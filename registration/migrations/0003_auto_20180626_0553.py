# Generated by Django 2.0.6 on 2018-06-26 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_consumer_badge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumer',
            name='badge',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]