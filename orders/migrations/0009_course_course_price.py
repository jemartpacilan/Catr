# Generated by Django 2.0.6 on 2018-07-13 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20180711_0658'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_price',
            field=models.DecimalField(decimal_places=2, default=10.0, max_digits=7),
            preserve_default=False,
        ),
    ]