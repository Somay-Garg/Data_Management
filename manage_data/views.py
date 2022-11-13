from operator import or_
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import *
from .forms import *
from django.db.models import Q
import json
# Create your views here.

def index(request):
    return render(request,'index.html')

def display_events(request):
    fields = Events._meta.fields
    event_data = Events.objects.all().values()
    
    filter_data = {
        'Event Name': set(),
        'Event Type': set(),
        'Audience': set(),
        'break' : 1,
        'Organized By': set(),
        'Conducted By': set(),
        'Sponsors' : set(),
        'break' : 1,
    }

    for event in event_data:
        filter_data['Event Name'].add(event['event_name'])
        filter_data['Event Type'].add(event['type_of_event'])
        filter_data['Audience'].add(event['Audience'])
        filter_data['Organized By'].add(event['Organized_by'])
        filter_data['Conducted By'].add(event['Conducted_by'])

        sponsors = json.loads(event['sponsors_details'])
        for sponsor in sponsors:
            filter_data['Sponsors'].add(sponsor)

    context = {
        'fields' : fields,
        'event_data' : event_data,
        'header' : 'Events',
        'filter_data' : filter_data,
        'sponsors' : sponsors,
    }

    return render(request,'index.html',context)

def filter_events(request):
    if request.method == "POST":

        if(request.POST['filter'] == "reset"):
            return redirect('display_events')
        
        event_name = request.POST['Event Name']
        type_of_event = request.POST['Event Type']
        Audience = request.POST['Audience']
        Organized_by = request.POST['Organized By']
        Conducted_by = request.POST['Conducted By']
        sponsored_by = request.POST['Sponsors']
        after = request.POST['after']
        upto = request.POST['upto']
        query = Q()

        sel_fil_val = {
            'Event Name': '-1',
            'Event Type': '-1',
            'Audience': '-1',
            'Organized By': '-1',
            'Conducted By': '-1',
            'Sponsors' : '-1',
        }

        if(event_name != "-1"):
            query = query & Q(event_name = event_name)
            sel_fil_val['Event Name'] = event_name
        if(type_of_event != "-1"):
            query = query & Q(type_of_event = type_of_event)
            sel_fil_val['Event Type'] = type_of_event
        if(Audience != "-1"):
            query = query & Q(Audience__in = ["both",Audience])
            sel_fil_val['Audience'] = Audience
        if(Organized_by != "-1"):
            query = query & Q(Organized_by = Organized_by)
            sel_fil_val['Organized By'] = Organized_by
        if(Conducted_by != "-1"):
            query = query & Q(Conducted_by = Conducted_by)
            sel_fil_val['Conducted By'] = Conducted_by
        if(sponsored_by != "-1"):
            query = query & Q(sponsors_details__contains = sponsored_by)
            sel_fil_val['Sponsors'] = sponsored_by
        if(after == ''):
            after = '1900-01-01'
        else:
            sel_fil_val['start_date'] = after
        if(upto == ''):
            upto = '2100-01-01'
        else:
            sel_fil_val['end_date'] = upto
        
        query2 = Q(start_date__range=[after,upto]) | Q(end_date__range=[after,upto])

        fields = Events._meta.fields
        all_data = Events.objects.all().values()
        
        filter_data = {
            'Event Name': set(),
            'Event Type': set(),
            'Audience': set(),
            'break' : 1,
            'Organized By': set(),
            'Conducted By': set(),
            'Sponsors' : set(),
            'break' : 1,
        }

        for event in all_data:
            filter_data['Event Name'].add(event['event_name'])
            filter_data['Event Type'].add(event['type_of_event'])
            filter_data['Audience'].add(event['Audience'])
            filter_data['Organized By'].add(event['Organized_by'])
            filter_data['Conducted By'].add(event['Conducted_by'])
            
            sponsors = json.loads(event['sponsors_details'])
            for sponsor in sponsors:
                filter_data['Sponsors'].add(sponsor)

        event_data = Events.objects.filter(query & query2).values()

        context = {
            'fields' : fields,
            'event_data' : event_data,
            'header' : 'Events',
            'filter_data' : filter_data,
            'sel_fil_val' : sel_fil_val,
            'sponsors' : sponsors,
        }

        # print(context)

        return render(request,'index.html',context)
    else:
        return render(request,'add_event.html',{})


def add_event(request):
    if request.method == "POST":
        event_name = request.POST['event_name']
        type_of_event = request.POST['type_of_event']
        Audience = request.POST['audience']
        Organized_by = request.POST['org_by']
        Conducted_by = request.POST['cond_by']
        no_of_sponsors = request.POST['no_of_sponsors']
        sponsors_details = request.POST['sponsored_dets']
        total_sponsored_amt = request.POST['total_sponsored_amt']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        no_of_participants = request.POST['no_of_parti']
        upload_attendance = ''

        if request.method == 'POST' and request.FILES['upload_atten']:
            upload_attendance = request.FILES['upload_atten']
            fs = FileSystemStorage(location='attendance/event_attendances/')
            filename = fs.save(upload_attendance.name, upload_attendance)
            uploaded_file_url = fs.url(filename)
            upload_attendance = uploaded_file_url

        event = Events(
            event_name=event_name,
            type_of_event=type_of_event,
            Audience=Audience,
            Organized_by=Organized_by,
            Conducted_by=Conducted_by,
            no_of_sponsors=no_of_sponsors,
            sponsors_details=sponsors_details,
            total_sponsored_amt=total_sponsored_amt,
            start_date=start_date,
            end_date=end_date,
            no_of_participants=no_of_participants,
            upload_attendance='attendance/event_attendances'+upload_attendance
        )
        event.save()
        return redirect('display_events')
    else:
        return render(request,'add_event.html',{})

def edit_form(request,pk,model,cls):
    item = get_object_or_404(model,pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('display_events')
        else:
            return redirect('display_events')

    else:
        form = cls(instance=item)
        return render(request,'edit_item.html',{'form' : form})

def edit_event(request,pk):
    return edit_form(request,pk,Events,EventForm)

def delete_entry(request,pk,model,header):
    model.objects.filter(id=pk).delete()
    return display_events(request)

def delete_event(request,pk):
    return delete_entry(request,pk,Events,"Events")