from operator import or_
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import *
from .forms import *
from django.db.models import Q
from django.template.defaulttags import register

# Create your views here.

def index(request):
    return render(request,'index.html')

def display_laptops(request):
    fields = Laptop._meta.fields
    items = Laptop.objects.all()
    req = ['type','price']

    context = {
        'items' : items,
        'header' : "Laptops",
        'fields' : fields,
        'req' : req,
    }

    return render(request,'index.html',context)

def display_desktops(request):
    items = Desktop.objects.all()
    fields = Desktop._meta.fields

    context = {
        'items' : items,
        'header' : "Desktops",
        'fields' : fields,
    }

    return render(request,'index.html',context)

def display_mobiles(request):
    items = Mobile.objects.all()
    fields = Mobile._meta.fields

    context = {
        'items' : items,
        'header' : "Mobiles",
        'fields' : fields
    }

    return render(request,'index.html',context)

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
        filter_data['Sponsors'].update(set(event['sponsored_by'].split(',')))

    context = {
        'fields' : fields,
        'event_data' : event_data,
        'header' : 'Events',
        'filter_data' : filter_data,
    }

    return render(request,'index.html',context)

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

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
            query = query & Q(sponsored_by__contains = sponsored_by)
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
            filter_data['Sponsors'].update(set(event['sponsored_by'].split(',')))

        event_data = Events.objects.filter(query & query2).values()

        context = {
            'fields' : fields,
            'event_data' : event_data,
            'header' : 'Events',
            'filter_data' : filter_data,
            'sel_fil_val' : sel_fil_val,
        }

        return render(request,'index.html',context)
    else:
        return render(request,'add_event.html',{})

def add_device(request,cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('display_laptops')
        else:
            return redirect('display_laptops')

    else:
        form = cls()
        return render(request,'add_new.html',{'form': form})

def add_laptop(request):
    return add_device(request,LaptopForm)

def add_desktop(request):
    return add_device(request,DesktopForm)

def add_mobile(request):
    return add_device(request,MobileForm)

def add_event(request):
    if request.method == "POST":
        event_name = request.POST['event_name']
        type_of_event = request.POST['type_of_event']
        Audience = request.POST['audience']
        Organized_by = request.POST['org_by']
        Conducted_by = request.POST['cond_by']
        no_of_sponsors = request.POST['no_of_sponsors']
        sponsored_by = ', '.join(request.POST.getlist('spon_by'))
        amt_of_sponsorship = request.POST['amt_of_spon']
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
            sponsored_by=sponsored_by,
            amt_of_sponsorship=amt_of_sponsorship,
            start_date=start_date,
            end_date=end_date,
            no_of_participants=no_of_participants,
            upload_attendance='attendance/event_attendances'+upload_attendance
        )
        event.save()
        return redirect('display_laptops')
    else:
        return render(request,'add_event.html',{})

def edit_device(request,pk,model,cls):
    item = get_object_or_404(model,pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('display_laptops')
        else:
            return redirect('display_laptops')

    else:
        form = cls(instance=item)
        return render(request,'edit_item.html',{'form' : form})

def edit_laptop(request,pk):
    return edit_device(request,pk,Laptop,LaptopForm)

def edit_desktop(request,pk):
    return edit_device(request,pk,Desktop,DesktopForm)

def edit_mobile(request,pk):
    return edit_device(request,pk,Mobile,MobileForm)

def edit_event(request,pk):
    return edit_device(request,pk,Events,EventForm)

def delete_device(request,pk,model,header):
    model.objects.filter(id=pk).delete()
    fields = model._meta.fields

    items = model.objects.all()

    context = {
        'fields' : fields,
        'items' : items,
        'header' : header,
    }

    return render(request,'index.html',context)

def delete_laptop(request,pk):
    return delete_device(request,pk,Laptop,"Laptops")

def delete_desktop(request,pk):
    return delete_device(request,pk,Desktop,"Desktops")

def delete_mobile(request,pk):
    return delete_device(request,pk,Mobile,"Mobiles")

def delete_event(request,pk):
    return delete_device(request,pk,Events,"Events")
