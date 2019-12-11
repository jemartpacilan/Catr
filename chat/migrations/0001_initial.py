# Generated by Django 2.0.6 on 2018-07-13 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0018_transaction_caterer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_body', models.CharField(max_length=1000)),
                ('message_date_submitted', models.DateTimeField()),
                ('caterer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Caterer')),
                ('consumer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.Consumer')),
            ],
        ),
    ]