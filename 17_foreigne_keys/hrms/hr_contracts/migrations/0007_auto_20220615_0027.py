# Generated by Django 2.0 on 2022-06-14 17:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hr_contracts', '0006_auto_20220615_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractmodel',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2022, 6, 14, 17, 57, 39, 806105, tzinfo=utc), verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='contractmodel',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2022, 6, 14, 17, 57, 39, 806105, tzinfo=utc), verbose_name='Start Date'),
        ),
    ]
