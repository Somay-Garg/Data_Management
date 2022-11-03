from operator import or_
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import *
from .forms import *
import os
# Create your views here.

def index(request):
    return render(request,'index.html')

def display_events(request):
    fields = Events._meta.fields
    event_data = Events.objects.all().values()
    context = {
        'fields' : fields,
        'event_data' : event_data,
        'header' : 'Events',
    }

    # print(type(event_data))

    return render(request,'index.html',context)

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
    fields = model._meta.fields

    items = model.objects.all()

    context = {
        'fields' : fields,
        'items' : items,
        'header' : header,
    }

    return render(request,'index.html',context)

def delete_event(request,pk):
    return delete_entry(request,pk,Events,"Events")
