# Generated by Django 4.1.2 on 2023-03-05 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_data', '0012_alter_events_upload_report'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.AlterField(
            model_name='studentcurrentstatushighedudetails',
            name='id_proof',
            field=models.FileField(blank=True, null=True, upload_to='placements/id_proof/'),
        ),
        migrations.AlterField(
            model_name='studentcurrentstatusjobdetails',
            name='joining_proof',
            field=models.FileField(blank=True, null=True, upload_to='placements/joining_proof/'),
        ),
        migrations.AlterField(
            model_name='studentexamdetails',
            name='result_proof',
            field=models.FileField(blank=True, null=True, upload_to='placements/result_proof/'),
        ),
        migrations.AlterField(
            model_name='studentofferdetails',
            name='job_proof',
            field=models.FileField(upload_to='placements/job_proof/'),
        ),
        migrations.AlterField(
            model_name='studentofferdetails',
            name='package_in_lpa',
            field=models.DecimalField(decimal_places=2, max_digits=19),
        ),
    ]