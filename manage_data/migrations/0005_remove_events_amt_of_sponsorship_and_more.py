# Generated by Django 4.0.3 on 2022-11-03 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_data', '0004_delete_desktop_delete_laptop_delete_mobile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='events',
            name='amt_of_sponsorship',
        ),
        migrations.RemoveField(
            model_name='events',
            name='sponsored_by',
        ),
        migrations.AddField(
            model_name='events',
            name='sponsors_details',
            field=models.CharField(default='Somay', max_length=255),
        ),
        migrations.AddField(
            model_name='events',
            name='total_sponsored_amt',
            field=models.IntegerField(default=0),
        ),
    ]
