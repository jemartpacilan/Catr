# Generated by Django 2.0.6 on 2018-07-03 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20180703_0049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='course',
            new_name='tray',
        ),
    ]
