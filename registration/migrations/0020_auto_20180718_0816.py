# Generated by Django 2.0.7 on 2018-07-18 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0019_auto_20180718_0156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(max_length=50)),
                ('package_date_created', models.DateTimeField()),
                ('caterer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Caterer')),
            ],
        ),
        migrations.AlterField(
            model_name='menu',
            name='package',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='registration.Package'),
        ),
    ]
