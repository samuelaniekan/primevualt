# Generated by Django 3.1.6 on 2021-03-16 15:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210316_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]