# Generated by Django 4.1.2 on 2023-01-15 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_data', '0012_rename_eroll_no_students_enroll_no_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='enroll_no',
            new_name='eroll_no',
        ),
        migrations.AlterField(
            model_name='students',
            name='position',
            field=models.CharField(choices=[('I', 'I'), ('II', 'II'), ('III', 'III'), ('Runner_up', 'Runner_up')], max_length=20),
        ),
    ]
