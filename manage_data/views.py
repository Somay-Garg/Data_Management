from operator import or_
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import *
from .forms import *
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import FileResponse
from django.forms.models import model_to_dict
from datetime import datetime
import json
import os
import csv
import uuid
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
        'break1' : 1,
        'Society' : set(),
        'Department' : set(),
        'Organized By': set(),
        'break2' : 1,
        'Conducted By': set(),
        'Sponsors' : set(),
        'break3' : 1,
    }

    sponsor = ''
    for event in event_data:
        filter_data['Event Name'].add(event['event_name'])
        filter_data['Event Type'].add(event['type_of_event'])
        filter_data['Audience'].add(event['Audience'])

        socities = event['Societies'].split(',')
        for society in socities:
            filter_data['Society'].add(society)
        
        departments = event['Departments'].split(',')
        for department in departments:
            filter_data['Department'].add(department)
        
        filter_data['Organized By'].add(event['Organized_by'])
        filter_data['Conducted By'].add(event['Conducted_by'])
        sponsor = json.loads(event['sponsors_details'])
        for spon in sponsor:
            filter_data['Sponsors'].add(spon)

    for event in event_data:
        event['sponsors_details'] = json.loads(event['sponsors_details'])
        # event['upload_attendance_dis'] = event['upload_attendance'].split('/')[-1]
        # event['upload_report_dis'] = event['upload_report'].split('/')[-1]

    context = {
        'fields' : fields,
        'event_data' : event_data,
        'header' : 'Events',
        'filter_data' : filter_data,
        'sponsors' : sponsor,
    }

    # path = os.path.realpath(os.path.dirname(__file__))
    # for event in event_data:
    #     atten = path
    #     for folder in event['upload_attendance'].split('/'): 
    #         atten = os.path.join(atten,folder)   
    #     event['upload_attendance_link'] = atten

    return render(request,'index.html',context)

def filter_events(request):
    if request.method == "POST":
        if(request.POST['filter'] == "reset"):
            return redirect('display_events')

        if(request.POST['filter'] == "export"):
            # if not request.POST['export_filter']:
            return export_data(request)
        
        if(request.POST['filter'] == "export"):
            return export_data(request)

        event_name = request.POST['Event Name']
        type_of_event = request.POST['Event Type']
        Audience = request.POST['Audience']
        Society = request.POST['Society']
        Department = request.POST['Department']
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
            'Society': '-1',
            'Department': '-1',
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
        if(Society != "-1"):
            query = query & Q(Societies__contains = Society)
            sel_fil_val['Society'] = Society
        if(Department != "-1"):
            query = query & (Q(Departments__contains = "All") | Q(Departments__contains = Department))
            sel_fil_val['Department'] = Department
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
        event_data = Events.objects.filter(query & query2).values()

        fields = Events._meta.fields
        all_data = Events.objects.all().values()
        
        filter_data = {
            'Event Name': set(),
            'Event Type': set(),
            'Audience': set(),
            'break1' : 1,
            'Society' : set(),
            'Department' : set(),
            'Organized By': set(),
            'break2' : 1,
            'Conducted By': set(),
            'Sponsors' : set(),
            'break3' : 1,
        }

        sponsor = ''
        for event in all_data:
            filter_data['Event Name'].add(event['event_name'])
            filter_data['Event Type'].add(event['type_of_event'])
            filter_data['Audience'].add(event['Audience'])

            socities = event['Societies'].split(',')
            for society in socities:
                filter_data['Society'].add(society)
            
            departments = event['Departments'].split(',')
            for department in departments:
                filter_data['Department'].add(department)

            filter_data['Organized By'].add(event['Organized_by'])
            filter_data['Conducted By'].add(event['Conducted_by'])
            sponsor = json.loads(event['sponsors_details'])
            for spon in sponsor:
                filter_data['Sponsors'].add(spon)

        for event in event_data:
            event['sponsors_details'] = json.loads(event['sponsors_details'])

        context = {
            'fields' : fields,
            'event_data' : event_data,
            'header' : 'Events',
            'filter_data' : filter_data,
            'sel_fil_val' : sel_fil_val,
            'sponsors' : sponsor,
            'sel_fil_val_json_string' : json.dumps(sel_fil_val),
        }

        return render(request,'index.html',context)
    else:
        return render(request,'add_event.html',{})

def add_event(request):
    if request.method == "POST":
        event_name = request.POST['event_name']
        type_of_event = request.POST['type_of_event']
        Audience = request.POST['audience']
        Societies = request.POST['society']
        Departments = request.POST['department']
        Organized_by = request.POST['org_by']
        Conducted_by = request.POST['cond_by']
        no_of_sponsors = request.POST['no_of_sponsors']
        sponsors_details = request.POST['sponsored_dets']
        total_sponsored_amt = request.POST['total_sponsored_amt']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        no_of_participants = request.POST['no_of_parti']
        upload_attendance = ''
        upload_report = ''

        now = datetime.now()

        if request.method == 'POST' and request.FILES['upload_atten']:
            upload_attendance = request.FILES['upload_atten']
            fs = FileSystemStorage(location='attendance/event_attendances/')
            filename = fs.save(now.strftime("%H%M%S")+"_"+upload_attendance.name, upload_attendance)
            uploaded_file_url = fs.url(filename)
            upload_attendance = uploaded_file_url.split('/')[-1]
        
        if request.method == 'POST' and request.FILES['upload_report']:
            upload_report = request.FILES['upload_report']
            fs = FileSystemStorage(location='report/event_reports/')
            filename = fs.save(now.strftime("%H%M%S")+"_"+upload_report.name, upload_report)
            uploaded_file_url = fs.url(filename)
            upload_report = uploaded_file_url.split('/')[-1]

        event = Events(
            event_name=event_name,
            type_of_event=type_of_event,
            Audience=Audience,
            Societies=Societies,
            Departments=Departments,
            Organized_by=Organized_by,
            Conducted_by=Conducted_by,
            no_of_sponsors=no_of_sponsors,
            sponsors_details=sponsors_details,
            total_sponsored_amt=total_sponsored_amt,
            start_date=start_date,
            end_date=end_date,
            no_of_participants=no_of_participants,
            upload_attendance=upload_attendance,
            upload_report=upload_report
        )
        
        event.save()
        return redirect('display_events')
    else:
        return render(request,'add_event.html',{})

def edit_form(request,pk,model,cls):
    item = get_object_or_404(model,pk=pk)
    print(item.Societies)
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

def export_data(request):
    filter_data = request.POST['filter_data']
    req_col = []
    if request.POST['display_columns'] == 'All':
        fields = Events._meta.fields
        for field in fields:
            if field.name != "id" and field.name != "upload_attendance" and field.name != "upload_report" and field.name != "uploaded_at":
                req_col.append(field.name)
    else:
        req_col = request.POST['display_columns'].split(',')

    query = Q()
    print(filter_data)
    if filter_data == "All":
        query2 = Q()
    else:
        filter_data = json.loads(filter_data)

        event_name = filter_data['Event Name']
        type_of_event = filter_data['Event Type']
        Audience = filter_data['Audience']
        Society = filter_data['Society']
        Department = filter_data['Department']
        Organized_by = filter_data['Organized By']
        Conducted_by = filter_data['Conducted By']
        sponsored_by = filter_data['Sponsors']
        if 'after' in filter_data:
            after = filter_data['after']
        else:
            after = '1900-01-01'
        if 'upto' in filter_data:
            upto = filter_data['upto']
        else:
            upto = '2100-01-01'
        if(event_name != "-1"):
            query = query & Q(event_name = event_name)
        if(type_of_event != "-1"):
            query = query & Q(type_of_event = type_of_event)
        if(Audience != "-1"):
            query = query & Q(Audience__in = ["both",Audience])
        if(Society != "-1"):
            query = query & Q(Societies__contains = Society)
        if(Department != "-1"):
            query = query & (Q(Departments__contains = "All") | Q(Departments__contains = Department))
        if(Organized_by != "-1"):
            query = query & Q(Organized_by = Organized_by)
        if(Conducted_by != "-1"):
            query = query & Q(Conducted_by = Conducted_by)
        if(sponsored_by != "-1"):
            query = query & Q(sponsors_details__contains = sponsored_by)
        
        query2 = Q(start_date__range=[after,upto]) | Q(end_date__range=[after,upto])
    
    event_data = Events.objects.filter(query & query2).values(*req_col)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=events.csv'
    
    writer = csv.writer(response)
    req_col.insert(0,'S.no')
    writer.writerow(req_col)

    writer.writerow([])

    i = 1
    for event in event_data:
        event_row = [i]
        for value in event:
            event_row.append(event[value])
            print(event[value])
        writer.writerow(event_row)
        i+=1

    return response

def open_file_atten(request,file):
    return FileResponse(open('attendance/event_attendances/'+file, 'rb'), filename=file)

def open_file_report(request,file):
    return FileResponse(open('report/event_reports/'+file, 'rb'), filename=file)
