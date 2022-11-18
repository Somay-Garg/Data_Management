# Generated by Django 4.1.2 on 2022-11-14 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_data', '0004_delete_desktop_delete_laptop_delete_mobile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='Departments',
            field=models.CharField(choices=[('CSE', 'CSE'), ('IT', 'IT'), ('ECE', 'ECE'), ('EEE', 'EEE'), ('Applied Science', 'Applied Science'), ('All', 'All'), ('None', 'None')], default='None', max_length=255),
        ),
        migrations.AddField(
            model_name='events',
            name='Societies',
            field=models.CharField(choices=[('Prakriti', 'Prakriti'), ('E-Cell', 'E-Cell'), ('IIC', 'IIC'), ('NISP', 'NISP'), ('UBA', 'UBA'), ('E-yantra', 'E-yantra'), ('EBSB', 'EBSB'), ('IIIC', 'IIIC'), ('TechSoc', 'TechSoc'), ('Mutants', 'Mutants'), ('Veda', 'Veda'), ('NSS', 'NSS'), ('None', 'None')], default='None', max_length=255),
        ),
        migrations.AddField(
            model_name='events',
            name='upload_report',
            field=models.FileField(blank=True, upload_to='report/event_reports/'),
        ),
    ]
