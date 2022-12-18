from django import forms
from .models import *
import datetime

class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('event_name','type_of_event','Audience','Societies','Departments','Organized_by','Conducted_by','no_of_sponsors','sponsors_details','total_sponsored_amt','start_date','end_date','no_of_participants','upload_attendance','upload_report')

def possible_years(first_year_in_scroll,last_year_in_scroll):
    p_year=[]
    for i in range(first_year_in_scroll,last_year_in_scroll,-1):
        p_year_tuple=str(i),i
        p_year.append(p_year_tuple)
    return p_year    

class InfraForm(forms.ModelForm):
    year_of_establishment=forms.ChoiceField(choices=possible_years(((datetime.now()).year),1984))           