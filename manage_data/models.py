from unittest.util import _MAX_LENGTH
from django.db import models
# Create your models here.

class Device(models.Model):
    type = models.CharField(max_length=100,blank=False)
    price = models.IntegerField()

    choices = (
        ('AVAILABLE','Item ready to be purchased'),
        ('SOLD','Item Sold'),
        ('RESTOCKING','Item restocking in a few days')
    )
    
    status = models.CharField(max_length=10,choices=choices,default="SOLD")
    issues = models.CharField(max_length=100,default="No issues")

    class Meta:
        abstract = True

    def __str__(self):
        return 'Type : {0} Price : {1}'.format(self.type,self.price)


class Laptop(Device):
    pass

class Desktop(Device):
    pass

class Mobile(Device):
    pass

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
    sponsored_by = models.CharField(max_length=255,blank=False)
    amt_of_sponsorship = models.CharField(max_length=255,blank=False)
    start_date = models.DateField()
    end_date = models.DateField()
    no_of_participants = models.IntegerField()
    upload_attendance = models.FileField(upload_to='attendance/event_attendances/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event_name