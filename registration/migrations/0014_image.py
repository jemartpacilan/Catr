# Generated by Django 2.0.6 on 2018-07-10 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0013_auto_20180709_0231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_uploaded_date', models.DateTimeField()),
                ('image_binary', models.BinaryField()),
                ('image_name', models.CharField(max_length=100)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Menu')),
            ],
        ),
    ]
