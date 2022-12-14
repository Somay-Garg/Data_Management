from django import forms
from .models import *

class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('event_name','type_of_event','Audience','Societies','Departments','Organized_by','Conducted_by','no_of_sponsors','sponsors_details','total_sponsored_amt','start_date','end_date','no_of_participants','upload_attendance','upload_report')

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'