# Generated by Django 4.1.2 on 2022-12-18 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_data', '0009_remove_events_max_amount_remove_events_min_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('eroll_no', models.IntegerField()),
                ('semester', models.IntegerField(max_length=2)),
                ('Departments', models.CharField(choices=[('CSE', 'CSE'), ('IT', 'IT'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('Applied Science', 'Applied Science'), ('All', 'All'), ('None', 'None')], default='None', max_length=255)),
                ('Class', models.CharField(choices=[('I', 'I'), ('II', 'II'), ('III', 'III'), ('Evening', 'Evening')], max_length=255)),
                ('mobile_no', models.IntegerField(max_length=10)),
                ('mail_id', models.EmailField(max_length=254)),
                ('event_name', models.CharField(max_length=255)),
                ('event_type', models.CharField(choices=[('Cultural', 'Cultural'), ('Technical', 'Technical'), ('Sports', 'Sports')], max_length=30)),
                ('event_date', models.DateField()),
                ('organised_by', models.CharField(max_length=255)),
                ('host_institute', models.CharField(max_length=255)),
                ('position', models.CharField(choices=[('I', 'I'), ('II', 'II'), ('III', 'III'), ('None', 'None')], max_length=20)),
                ('team_size', models.CharField(choices=[('Team', 'Team'), ('Individual', 'Individual')], max_length=20)),
                ('level', models.CharField(choices=[('College', 'College'), ('InterCollege', 'InterCollege'), ('University', 'University'), ('State', 'State'), ('National', 'National'), ('International', 'International')], default='College', max_length=30)),
                ('date_of_award', models.DateField()),
                ('upload_proof', models.CharField(max_length=255)),
            ],
        ),
    ]
