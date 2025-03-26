# Generated by Django 5.1.6 on 2025-03-26 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_auto_20250326_1304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='reservation_date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='reservation_slot',
        ),
        migrations.AddField(
            model_name='booking',
            name='comment',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='booking',
            name='guest_number',
            field=models.IntegerField(default=''),
        ),
        migrations.AddField(
            model_name='booking',
            name='last_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='booking',
            name='first_name',
            field=models.CharField(default='', max_length=200),
        ),
    ]
