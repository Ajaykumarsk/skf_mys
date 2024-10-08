# Generated by Django 5.0.4 on 2024-07-30 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0005_rename_grace_period_after_start_time_autoshift_full_day_threshold_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='lunch_duration',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shift',
            name='lunch_in',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shift',
            name='lunch_out',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
