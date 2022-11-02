from unittest.util import _MAX_LENGTH
from django.db import models
# Create your models here.

class Events(models.Model):
    event_name = models.CharField(max_length=200,blank=False)
    type_of_event = models.CharField(max_length=200,blank=False)

    audience = (
        ('Faculty','Faculty'),
        ('Student','Student'),
        ('Both','Faculty and Student'),
    )
    Audience = models.CharField(max_length=20,choices=audience,blank=False)
    
    Organized_by = models.CharField(max_length=255,blank=False)
    Conducted_by = models.CharField(max_length=255,blank=False)
    no_of_sponsors = models.IntegerField()
    sponsors_details = models.CharField(max_length=255,blank=False,default='Somay')
    total_sponsored_amt = models.IntegerField(default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    no_of_participants = models.IntegerField()
    upload_attendance = models.FileField(upload_to='attendance/event_attendances/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event_name