# Generated by Django 4.1.2 on 2022-12-15 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_data', '0008_events_max_amount_events_min_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='max_amount',
        ),
        migrations.RemoveField(
            model_name='events',
            name='min_amount',
        ),
    ]
