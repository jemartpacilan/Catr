# Generated by Django 2.0.6 on 2018-07-03 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20180703_0049'),
        ('registration', '0007_menu_package'),
    ]

    operations = [
        migrations.AddField(
            model_name='consumer',
            name='history',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='orders.History'),
            preserve_default=False,
        ),
    ]
