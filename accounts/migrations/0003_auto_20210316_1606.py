# Generated by Django 3.1.6 on 2021-03-16 15:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210315_1723'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coupon',
            options={'ordering': ('-created', 'active')},
        ),
        migrations.AlterField(
            model_name='coupon',
            name='created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 3, 16, 15, 6, 14, 840652, tzinfo=utc)),
        ),
    ]
