# Generated by Django 2.0.6 on 2018-07-10 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0015_auto_20180710_0610'),
    ]

    operations = [
        migrations.AddField(
            model_name='catruser',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_binary',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
