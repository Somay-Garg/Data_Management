from unittest.util import _MAX_LENGTH
from django.db import models
from rest_framework import serializers
# Create your models here.

class Events(models.Model):
    event_name = models.CharField(max_length=200,blank=False)
    event_types = (
        ('Cultural','Cultural'),
        ('Technical','Technical'),
        ('Sports','Sports'),
        ('FDP','FDP'),
        ('Seminar','Seminar'),
        ('Workshop','Workshop'),
        ('Expert Lecture','Expert Lecture'),
        ('Conference','Conference'),
    )
    type_of_event = models.CharField(max_length=200,choices=event_types,blank=False)

    audience = (
        ('Faculty','Faculty'),
        ('Student','Student'),
        ('Both','Faculty and Student'),
    )
    Audience = models.CharField(max_length=20,choices=audience,blank=False)
    
    societies = (
        ('Prakriti','Prakriti'),
        ('E-Cell','E-Cell'),
        ('IIC','IIC'),
        ('NISP','NISP'),
        ('UBA','UBA'),
        ('E-yantra','E-yantra'),
        ('EBSB','EBSB'),
        ('IIIC','IIIC'),
        ('TechSoc','TechSoc'),
        ('Mutants','Mutants'),
        ('Veda','Veda'),
        ('NSS','NSS'),
        ('None','None'),
    )
   
    Societies = models.CharField(max_length=255,choices=societies,blank=False,default="None")
    departments = (
        ('CSE','CSE'),
        ('IT','IT'),
        ('ECE','ECE'),
        ('EEE','EEE'),
        ('Applied Science','Applied Science'),
        ('All','All'),
        ('None','None'),
    )
    Departments = models.CharField(max_length=255,choices=departments,blank=False,default="None")
    Organized_by = models.CharField(max_length=255,blank=False)
    Conducted_by = models.CharField(max_length=255,blank=False)
    no_of_sponsors = models.IntegerField()
    sponsors_details = models.CharField(max_length=255,blank=False,default='Somay')
    total_sponsored_amt = models.IntegerField(default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    no_of_participants = models.IntegerField()
    upload_attendance = models.CharField(max_length=255,blank=False)
    upload_report = models.CharField(max_length=255,blank=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.event_name


class EventSerializer(serializers.Serializer):
    event_name = serializers.CharField(max_length=200)
    event_types = (
        ('Cultural','Cultural'),
        ('Technical','Technical'),
        ('Sports','Sports'),
        ('FDP','FDP'),
        ('Seminar','Seminar'),
        ('Workshop','Workshop'),
        ('Expert Lecture','Expert Lecture'),
        ('Conference','Conference'),
    )
    type_of_event = serializers.CharField(max_length=200)

    audience = (
        ('Faculty','Faculty'),
        ('Student','Student'),
        ('Both','Faculty and Student'),
    )
    Audience = serializers.CharField(max_length=20)
    
    societies = (
        ('Prakriti','Prakriti'),
        ('E-Cell','E-Cell'),
        ('IIC','IIC'),
        ('NISP','NISP'),
        ('UBA','UBA'),
        ('E-yantra','E-yantra'),
        ('EBSB','EBSB'),
        ('IIIC','IIIC'),
        ('TechSoc','TechSoc'),
        ('Mutants','Mutants'),
        ('Veda','Veda'),
        ('NSS','NSS'),
        ('None','None'),
    )
   
    Societies = serializers.CharField(max_length=255)
    departments = (
        ('CSE','CSE'),
        ('IT','IT'),
        ('ECE','ECE'),
        ('EEE','EEE'),
        ('Applied Science','Applied Science'),
        ('All','All'),
        ('None','None'),
    )
    Departments = serializers.CharField(max_length=255)
    Organized_by = serializers.CharField(max_length=255)
    Conducted_by = serializers.CharField(max_length=255)
    no_of_sponsors = serializers.IntegerField()
    sponsors_details = serializers.CharField(max_length=255)
    total_sponsored_amt = serializers.IntegerField(default=0)
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    no_of_participants = serializers.IntegerField()
    upload_attendance = serializers.CharField()
    upload_report = serializers.CharField(max_length=255)
    uploaded_at = serializers.DateTimeField()
    min_amount = serializers.IntegerField(default=0)
    max_amount = serializers.IntegerField(default=0)
