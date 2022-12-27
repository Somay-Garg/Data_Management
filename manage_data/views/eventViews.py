from operator import or_
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from manage_data.models.eventsModel import *
from ..forms import *
from django.db.models import Q
from django.http import HttpResponse
from django.http import FileResponse
from datetime import datetime
import json
import csv
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request,'events/index.html')

def display_events(request,msg=''):
    fields = Events._meta.fields
    event_data = Events.objects.all().values()
    columns = ['id','event_name','type_of_event','Audience','Societies','Departments','Organized_by','Conducted_by','sponsors_details','total_sponsored_amt','start_date','end_date','no_of_participants','upload_attendance','upload_report']
    columns_str = 'id,event_name,type_of_event,Audience,Societies,Departments,Organized_by,Conducted_by,sponsors_details,total_sponsored_amt,start_date,end_date,no_of_participants,upload_attendance,upload_report'
    filter_data = {
        'Event Name': set(),
        'Event Type': set(),
        'break1' : 1,
        'Audience': set(),
        'Society' :set(),
        'break2' : 1,
        'Department' : set(),
        'Organized By': set(),
        'break3' : 1,
        'Conducted By': set(),
        'Sponsors' : set(),
        'break4' : 1,
        'Total Sponsored Amount':set(),
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

    context = {
        'fields' : fields,
        'event_data' : event_data,
        'header' : 'Events',
        'filter_data' : filter_data,
        'sponsors' : sponsor,
        'columns':columns,
        'display':True,
        'columns_str':columns_str,
        'msg':msg,
        'showFilters':False,
    }

    if context['msg'] == 'Filter removed' or context['msg'] == 'Filter Applied':
        context['showFilters'] = True

    return render(request,'events/index.html',context)

# display the selected columns
def display_columns(request,msg=''):
    fields = Events._meta.fields
    columns = ['id','event_name','type_of_event','Audience','Societies','Departments','Organized_by','Conducted_by','sponsors_details','total_sponsored_amt','start_date','end_date','no_of_participants','upload_attendance','upload_report']
    columns_str = 'id,event_name,type_of_event,Audience,Societies,Departments,Organized_by,Conducted_by,sponsors_details,total_sponsored_amt,start_date,end_date,no_of_participants,upload_attendance,upload_report'
    # print(' ---------  ',type(columns))

    if(request.method == "POST"):
        if( 'columns_details' in request.POST and request.POST['columns_details'] != ''):
            # print('cols_dets' , type(request.POST['columns_details']))
            columns = request.POST['columns_details'].split(',')        
   
    filter_data = {
        'Event Name': set(),
        'Event Type': set(),
        'break1' : 1,
        'Audience': set(),
        'Society' :set(),
        'break2' : 1,
        'Department' : set(),
        'Organized By': set(),
        'break3' : 1,
        'Conducted By': set(),
        'Sponsors' : set(),
        'break4' : 1,
        'Total Sponsored Amount':set(),
    }
    
    event_data_all = Events.objects.all().values()

    sponsor = ''
    for event in event_data_all:
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
        # changes
        filter_data['Total Sponsored Amount'].add(event['total_sponsored_amt'])
        sponsor = json.loads(event['sponsors_details'])
        for spon in sponsor:
            filter_data['Sponsors'].add(spon)

    for event in event_data_all:
        event['sponsors_details'] = json.loads(event['sponsors_details'])
   
    event_data = ''
    if 'filter_data' in request.POST:
        filterData = request.POST['filter_data']
        # print("filterData > ",filterData)
        query = Q()
        if filterData == "All":
            query2 = Q()
        else:
            filterData = json.loads(filterData)
            
            event_name = filterData['Event Name']
            type_of_event = filterData['Event Type']
            Audience = filterData['Audience']
            Society = filterData['Society']
            Department = filterData['Department']
            Organized_by = filterData['Organized By']
            Conducted_by = filterData['Conducted By']
            sponsored_by = filterData['Sponsors']
            if 'after' in filterData:
                after = filterData['after']
            else:
                after = '1900-01-01'
            if 'upto' in filterData:
                upto = filterData['upto']
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
    
        event_data = Events.objects.filter(query & query2).values(*columns)

        # print("hii",event_data)
    else:
        event_data = event_data_all

    # print("event_data  -> ",event_data)

    context = {
        'fields' : fields,
        'columns' : columns,
        'event_data' : event_data,
        'header' : 'Events',
        'filter_data' : filter_data,
        'sponsors' : sponsor,
        'display' : True,
        'columns_str':columns_str,
        'msg':msg,
        'showFilters':False,
    }

    if request.POST['show_filters'] == 'true'  or request.POST['show_filters'] == 'True' :
        context['showFilters'] = True

    if 'columns_details' in request.POST:
        context['columns_str'] = request.POST['columns_details']
    elif 'columns_details' not in request.POST:
        context['display'] = False

    return render(request,'events/index.html',context)

# add new event
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
        sponsors_details = request.POST['sponsored_details']
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
            upload_report= upload_report
        )
        event.save()
        return display_events(request,'Details Added')
    else:
        return render(request,'events/addEvent.html',{})

# filter event data
def filter_event(request):
    if request.method == "POST":
        if(request.POST['filter'] == "reset"):
            return display_columns(request,'Filter removed')

        if(request.POST['filter'] == "export"):
            return export_data(request)
        columns = ['id','event_name','type_of_event','Audience','Societies','Departments','Organized_by','Conducted_by','sponsors_details','total_sponsored_amt','start_date','end_date','no_of_participants','upload_attendance','upload_report']
        if('columns_details' in request.POST and request.POST['columns_details'] != ''):
            columns = request.POST['columns_details'].split(",")

        event_name = request.POST['Event Name']
        type_of_event = request.POST['Event Type']
        Audience = request.POST['Audience'] 
        Society = request.POST['Society']
        Department = request.POST['Department']
        Organized_by = request.POST['Organized By']
        Conducted_by = request.POST['Conducted By']
        total_sponsored_amt = request.POST['Total Sponsored Amount']
        sponsored_by = request.POST['Sponsors']
        after = request.POST['after']
        upto = request.POST['upto']
        min_amount = request.POST['min_amount']
        max_amount = request.POST['max_amount']
        
        query = Q()
        
        sel_fil_val = {
            'Event Name': '-1',
            'Event Type': '-1',
            'Audience': '-1',
            'Society' : '-1',
            'Department' : '-1',
            'Organized By': '-1',
            'Conducted By': '-1',
            'Sponsors' : '-1',
            'Total Sponsored Amount' : '-1',
            
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
        
        query3 = Q(total_sponsored_amt__range = [min_amount,max_amount])
    
        fields = Events._meta.fields
        all_data = Events.objects.all().values()
        filter_data = {
            'Event Name': set(),
            'Event Type': set(),
            'break1':1,
            'Audience': set(),
            'Society' : set(),
            'break2' : 1,
            'Department' : set(),
            'Organized By': set(),
            'break3' : 1,
            'Conducted By': set(),
            'Sponsors' : set(),
            'break4' : 1,   
            'Total Sponsored Amount':set(),         
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
            # change
            filter_data['Total Sponsored Amount'].add(event['total_sponsored_amt'])

            sponsor = json.loads(event['sponsors_details'])
            for spon in sponsor:
                filter_data['Sponsors'].add(spon)
        
        event_data = Events.objects.filter(query & query2 & query3).values()
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
            'columns':columns,
            'display':True,
            'msg':"Filter Applied",
            'showFilters':True,
        }
        
        if('columns_details' in request.POST):
            context['columns_str'] = request.POST['columns_details']
        return render(request,'events/index.html',context)
    else:
        return render(request,'events/addEvent.html',{})

# open file 
def open_file_atten(request,file):
    return FileResponse(open('attendance/event_attendances/'+file, 'rb'), filename=file)

# open report
def open_file_report(request,file):
    return FileResponse(open('report/event_reports/'+file, 'rb'), filename=file)

def export_data(request):
    filter_data = request.POST['filter_data']
    req_col = []

    if 'columns_details' in request.POST:
        req_col = request.POST['columns_details'].split(',')
        print('required cols',req_col)
        req_col.remove('id')
    query = Q()
    # print(filter_data)
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

# for updating /editing 
def save_event(request,pk):
    item = Events.objects.get(id=pk)
    if request.method == "POST":
        item.event_name = request.POST['event_name']
        item.type_of_event = request.POST['type_of_event']
        item.Audience =request.POST['Audience']
        item.Societies = request.POST['Societies']
        item.Departments = request.POST['Departments']
        item.Organized_by = request.POST['Organized_by']
        item.Conducted_by = request.POST['Conducted_by']
        item.no_of_sponsors = request.POST['no_of_sponsors']
        item.sponsors_details = request.POST['sponsors_details']
        item.total_sponsored_amt = request.POST['total_sponsored_amt']
        item.start_date = request.POST['start_date']
        item.end_date = request.POST['end_date']
        item.no_of_participants = request.POST['no_of_participants']

        now = datetime.now()
        if request.method == 'POST' and "upload_attendance" in request.FILES and request.FILES['upload_attendance']:
            upload_attendance = request.FILES['upload_attendance']
            fs = FileSystemStorage(location='attendance/event_attendances/')
            filename = fs.save(now.strftime("%H%M%S")+"_"+upload_attendance.name, upload_attendance)
            uploaded_file_url = fs.url(filename)
            fs.delete(item.upload_attendance)
            item.upload_attendance = uploaded_file_url.split('/')[-1]
        
        if request.method == 'POST' and "upload_report" in request.FILES and request.FILES['upload_report']:
            upload_report = request.FILES['upload_report']
            fs = FileSystemStorage(location='report/event_reports/')
            filename = fs.save(now.strftime("%H%M%S")+"_"+upload_report.name, upload_report)
            uploaded_file_url = fs.url(filename)
            fs.delete(item.upload_report)
            item.upload_report = uploaded_file_url.split('/')[-1] 
        print("item saved")
        item.save()
        return display_columns(request,"Details Edited")
    else:
        form = EventForm(instance=item)
        return redirect(request,'events/edit_event.html',{'form':form},permanent=True)
    
def edit_event(request):
    id = request.POST['id_details']
    columns = request.POST['passingColumns']
    showFilters = request.POST['show_filters']
    print(showFilters)
    item = Events.objects.get(pk = id)
    form = EventForm(instance=item)
    context = {
        'form':form,
        'columns':columns,
        'id':id,
        'showFilters':showFilters,
    }
    return render(request,'events/edit_event.html',context)

# for deleting event entry
def delete_event_entry(request):
    if request.method == "POST":
        id = request.POST['id_details']
        columns = request.POST['columns_details'].split(',')
        item = get_object_or_404(Events,pk=id)
        fs_attendance = FileSystemStorage(location='attendance/event_attendances/')
        path_atten = str(item.upload_attendance)
        fs_attendance.delete(path_atten)
        fs_report = FileSystemStorage(location='report/event_reports/')
        path_report = str(item.upload_report)
        fs_report.delete(path_report)
        # print("helo",path_)
        show_filters = request.POST['show_filters']
        # print('hiii',show_filters)
        Events.objects.filter(id=id).delete()
        return display_columns(request,'Details Deleted')
    else:
        return HttpResponse(True)