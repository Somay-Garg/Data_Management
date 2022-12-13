# Generated by Django 4.1.2 on 2022-11-21 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_data', '0006_alter_events_upload_attendance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='type_of_event',
            field=models.CharField(choices=[('Cultural', 'Cultural'), ('Technical', 'Technical'), ('Sports', 'Sports'), ('FDP', 'FDP'), ('Seminar', 'Seminar'), ('Workshop', 'Workshop'), ('Expert Lecture', 'Expert Lecture'), ('Conference', 'Conference')], max_length=200),
        ),
    ]