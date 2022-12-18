from operator import or_
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from manage_data.models.studentsModel import *
from ..forms import *
from django.db.models import Q
from django.http import HttpResponse
from django.http import FileResponse
from datetime import datetime
import json
import csv
from django.views.decorators.csrf import csrf_exempt


def display_students(request):
    return render(request,'students/index.html')

def add_student(request):
    if request.method == "POST":
        # print('post data recieved')
        name = request.POST['name']
        eroll_no = request.POST['eroll_no']
        semester = request.POST['semester']
        Departments = request.POST['Departments']
        Class = request.POST['Class']
        mobile_no = request.POST['mobile_no']
        mail_id = request.POST['mail_id']
        event_name = request.POST['event_name']
        event_type = request.POST['event_type']
        event_date = request.POST['event_date']
        organized_by = request.POST['organized_by']
        host_institute = request.POST['host_institute']
        position = request.POST['position']
        team_size = request.POST['team_size']
        level = request.POST['level']
        date_of_award = request.POST['date_of_award']
        upload_proof = ''
        now = datetime.now()

        if request.method == 'POST' and request.FILES['upload_proof']:
            upload_proof = request.FILES['upload_proof']
            print("heelloo")
            fs = FileSystemStorage(location='proof/award_proof/')
            filename = fs.save(now.strftime("%H%M%S")+"_"+upload_proof.name, upload_proof)
            uploaded_file_url = fs.url(filename)
            upload_proof = uploaded_file_url.split('/')[-1]
        
        student = Students(
            name = name,
            eroll_no = eroll_no,
            semester = semester,
            Departments = Departments,
            Class = Class,
            mobile_no = mobile_no,
            mail_id = mail_id,
            event_name = event_name,
            event_type = event_type,
            event_date = event_date,
            organized_by = organized_by,
            host_institute = host_institute,
            position= position,
            team_size = team_size,
            level = level,
            date_of_award = date_of_award,
            upload_proof = upload_proof,
        )
        print('item saved')
        student.save()
        return redirect('display_students')
    else:
        return render(request,'students/addStudent.html',{})
def display_students_table(request):
    
    fields = Students._meta.fields
    columns = []
    if request.method == "POST":
        if 'columns_details' in request.POST:
            columns = request.POST['columns_details'].split(",")
        

    students_data = Students.objects.values(*columns)
    print("helloo",students_data)
        
    context = {
        'fields' : fields,
        'columns' : columns,
        'students_data':students_data,
        'header' : 'Students',
        'display' : True,
    }

    if 'columns_details' in request.POST:
        context['columns_str'] = request.POST['columns_details']
    elif 'columns_details' not in request.POST:
        context['display'] = False
        
    return render(request,'students/index.html',context)