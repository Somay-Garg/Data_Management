# Generated by Django 4.1.2 on 2023-01-11 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_data', '0010_alter_student_dob_alter_student_fname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentplacement',
            name='current_status',
            field=models.CharField(choices=[('Job', 'Job'), ('Higher Education', 'Higher Education'), ('Entreprenurship', 'Entreprenurship'), ('Others', 'Others')], default='Others', max_length=50),
        ),
    ]
