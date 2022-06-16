# Generated by Django 2.2 on 2022-05-15 13:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sample_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='age',
            field=models.IntegerField(default=0, verbose_name='Age'),
        ),
        migrations.AddField(
            model_name='employee',
            name='birthday',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Birthday'),
        ),
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(default='test@gmail.com', max_length=50),
        ),
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(default=None, upload_to='', verbose_name='Image'),
        ),
    ]