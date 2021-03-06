# Generated by Django 2.0 on 2022-06-14 18:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hr_contracts', '0008_auto_20220615_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractmodel',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2022, 6, 14, 18, 2, 1, 620053, tzinfo=utc), verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='contractmodel',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2022, 6, 14, 18, 2, 1, 620053, tzinfo=utc), verbose_name='Start Date'),
        ),
    ]
