from django import forms
from .models import *

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = ('type','price','status','issues')

class DesktopForm(forms.ModelForm):
    class Meta:
        model = Desktop
        fields = ('type','price','status','issues')

class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = ('type','price','status','issues')

class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('event_name','type_of_event','Audience','Organized_by','Conducted_by','no_of_sponsors','sponsored_by','amt_of_sponsorship','start_date','end_date','no_of_participants','upload_attendance')