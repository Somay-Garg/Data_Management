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

# display all the details nd columns
def display_students(request):
    fields = Students._meta.fields
    students_data = Students.objects.all().values()
    columns = ['id','name','eroll_no','semester','Departments','Class','organized_by','mobile_no','mail_id','event_name','event_type','event_date','host_institute','position','team_size','level','date_of_award','upload_proof']
    columns_str = 'id,name,eroll_no,semester,Departments,Class,organized_by,mobile_no,mail_id,event_name,event_type,event_date,host_institute,position,team_size,level,date_of_award,upload_proof'
    
    filter_data = {
        'Name': set(),
        'Semester':set(),
        'break1':1,
        'Departments':set(),
        'Class':set(),
        'break2':1,
        'Organized By':set(),
        'Event Name':set(),
        'break3':1,
        'Event Type':set(),
        'Host Institute':set(),
        'break4':1,
        'Position Obtained':set(),
        'Team Size':set(),
        'break5':1,
        'Level':set(),    
        'E-mail Id':set(),
        'break6':1,
        'Mobile No':set(),
        'Enrollment No':set(),
        'break7':1,
        'Award Date':set(),
        'Event Date':set(),
    }

    for student in students_data:
        filter_data['Name'].add(student['name'])
        filter_data['E-mail Id'].add(student['mail_id'])
        filter_data['Semester'].add(student['semester'])
        filter_data['Departments'].add(student['Departments'])
        filter_data['Class'].add(student['Class'])
        filter_data['Organized By'].add(student['organized_by'])
        filter_data['Event Name'].add(student['event_name'])
        filter_data['Event Type'].add(student['event_type'])
        filter_data['Host Institute'].add(student['host_institute'])
        filter_data['Position Obtained'].add(student['position'])
        filter_data['Team Size'].add(student['team_size'])
        filter_data['Level'].add(student['level'])
        filter_data['Event Date'].add(student['event_date'])
        filter_data['Award Date'].add(student['date_of_award'])
        filter_data['Mobile No'].add(student['mobile_no'])
        filter_data['Enrollment No'].add(student['eroll_no'])
        filter_data['E-mail Id'].add(student['mail_id'])

    context = {
        'fields' : fields,
        'students_data':students_data,
        'filter_data':filter_data,
        'header' : 'Students',
        'display':True,
        'columns':columns,        
        'columns_str':columns_str,
    }

    return render(request,'students/index.html',context)

def filter_student(request):    
    if request.method == 'POST':
        if request.POST['filter'] == 'reset':
            return redirect('display_students')
        if(request.POST['filter'] == "export"):
            return export_data(request)

        columns = ['id','name','eroll_no','semester','Departments','Class','organized_by','mobile_no','mail_id','event_name','event_type','event_date','host_institute','position','team_size','level','date_of_award','upload_proof']

        if('columns_details' in request.POST and request.POST['columns_details'] != ''):
            columns = request.POST['columns_details'].split(",")
        
        name = request.POST['Name']
        semester = request.POST['Semester']
        Departments = request.POST['Departments']
        Class = request.POST['Class']
        organized_by = request.POST['Organized By']
        event_name = request.POST['Event Name']
        event_type = request.POST['Event Type']
        host_institute = request.POST['Host Institute']
        position = request.POST['Position Obtained']
        team_size = request.POST['Team Size']
        level = request.POST['Level']
        mail_id = request.POST['E-mail Id']
        eroll_no = request.POST['Enrollment No']
        mobile_no = request.POST['Mobile No']
        date_of_award = request.POST['Award Date']
        event_date = request.POST['Event Date']
        
        students_data_all = Students.objects.all().values()

        filter_data = {
            'Name': set(),
            'Semester':set(),
            'break1':1,
            'Departments':set(),
            'Class':set(),
            'break2':1,
            'Organized By':set(),
            'Event Name':set(),
            'break3':1,
            'Event Type':set(),
            'Host Institute':set(),
            'break4':1,
            'Position Obtained':set(),
            'Team Size':set(),
            'break5':1,
            'Level':set(),    
            'E-mail Id':set(),
            'break6':1,
            'Mobile No':set(),
            'Enrollment No':set(),
            'break7':1,
            'Award Date':set(),
            'Event Date':set(),
        }

        for student in students_data_all:
            filter_data['Name'].add(student['name'])
            filter_data['E-mail Id'].add(student['mail_id'])
            filter_data['Semester'].add(student['semester'])
            filter_data['Departments'].add(student['Departments'])
            filter_data['Class'].add(student['Class'])
            filter_data['Organized By'].add(student['organized_by'])
            filter_data['Event Name'].add(student['event_name'])
            filter_data['Event Type'].add(student['event_type'])
            filter_data['Host Institute'].add(student['host_institute'])
            filter_data['Position Obtained'].add(student['position'])
            filter_data['Team Size'].add(student['team_size'])
            filter_data['Level'].add(student['level'])
            filter_data['Event Date'].add(student['event_date'])
            filter_data['Award Date'].add(student['date_of_award'])
            filter_data['Mobile No'].add(student['mobile_no'])
            filter_data['Enrollment No'].add(student['eroll_no'])
            filter_data['E-mail Id'].add(student['mail_id'])

        query = Q()        
        sel_fil_val = {
            'Name': '-1',
            'E-mail Id':'-1',
            'Semester':'-1',
            'Departments':'-1',
            'Class':'-1',
            'Organized By':'-1',
            'Event Name':'-1',
            'Event Type': '-1',
            'Host Institute':'-1',
            'Position Obtained':'-1',
            'Team Size':'-1',
            'Level':'-1',  
            'Event Date' :'-1',
            'Award Date' :'-1',
            'Mobile No' :'-1',
            'Enrollment No' :'-1',
            'E-mail Id' :'-1',
        }
        
        if(name != '-1'):
            query = query & Q(name = name)
            sel_fil_val['Name'] = name
        if( semester != '-1'):
            query = query & Q(semester = semester)
            sel_fil_val['Semester'] = semester
        if( Departments != '-1'):
            query = query & Q(Departments = Departments)
            sel_fil_val['Departments'] = Departments
        if( Class != '-1'):
            query = query & Q(Class = Class)
            sel_fil_val['Class'] = Class
        if( event_type != '-1'):
            query = query & Q(event_type = event_type)
            sel_fil_val['Event Type'] = event_type
        if( host_institute != '-1'):
            query = query & Q(host_institute = host_institute)
            sel_fil_val['Host Institute'] = host_institute
        if( organized_by != '-1'):
            query = query & Q(organized_by = organized_by)
            sel_fil_val['Organized By'] = organized_by
        if( position != '-1'):
            query = query & Q(position = position)
            sel_fil_val['Position Obtained'] = position
        if( team_size != '-1'):
            query = query & Q(team_size = team_size)
            sel_fil_val['Team Size'] = team_size
        if( level != '-1'):
            query = query & Q(level = level)
            sel_fil_val['Level'] = level
        if( mail_id != '-1' and mail_id != ''):
            query = query & Q(mail_id = mail_id)
            sel_fil_val['E-mail Id'] = mail_id
        if( eroll_no != '-1' and eroll_no != ''):
            query = query & Q(eroll_no = eroll_no)
            sel_fil_val['Enrollment No'] = eroll_no
        if( mobile_no != '-1' and mobile_no != ''):
            print("mobile",mobile_no)
            query = query & Q(mobile_no = mobile_no)
            sel_fil_val['Mobile No'] = mobile_no
        if( event_date != '-1' and event_date != ''):
            query = query & Q(event_date = event_date)
            sel_fil_val['Event Date'] = event_date
        if( date_of_award != '-1' and date_of_award != ''):
            query = query & Q(date_of_award = date_of_award)
            sel_fil_val['Award Date'] = date_of_award
        
        query2 = Q()
        students_data = Students.objects.filter(query).values()
        print("hello",query)

        fields = Students._meta.fields

        context = {
            'fields':fields,
            'students_data': students_data,
            'header':"Students",
            'filter_data':filter_data,
            'sel_fil_val':sel_fil_val,
            'sel_fil_val_json_string' : json.dumps(sel_fil_val),
            'columns':columns,
            'display':True,
        }
        
        if 'columns_details' in request.POST and request.POST['columns_details'] != '':
            context['columns_str'] = request.POST['columns_details']
        return render(request,'students/index.html',context)
    else:
        return render(request,'students/addStudent.html',{})

# add a new student entry
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
            # print("heelloo")
            fs = FileSystemStorage(location='proof/award_proof/')
            filename = fs.save(now.strftime("%H%M%S")+"_"+upload_proof.name, upload_proof)
            uploaded_file_url = fs.url(filename)
            upload_proof = uploaded_file_url.split('/')[-1]
            # print(upload_proof)
        
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
        # print('item saved')
        student.save()
        return redirect('display_students')
    else:
        return render(request,'students/addStudent.html',{})

# delete student entry
def delete_student_entry(request):
    if request.method == "POST":
        id = request.POST['id_details']
        columns = request.POST['columns_details'].split(',')
        item = get_object_or_404(Students,pk=id)
        fs_proof = FileSystemStorage(location='proof/award_proof/')
        path_ = str(item.upload_proof)
        # print("helo",path_)
        fs_proof.delete(path_)
        Students.objects.filter(id=id).delete()
        return display_students_table(request)
    else:
        return HttpResponse(True)

# display filtered columns
def display_students_table(request):   
    fields = Students._meta.fields
    columns = ['id','name','eroll_no','semester','Departments','Class','organized_by','mobile_no','mail_id','event_name','event_type','event_date','host_institute','team_size','level','date_of_award','upload_proof']
    columns_str = 'id,name,eroll_no,semester,Departments,Class,organized_by,mobile_no,mail_id,event_name,event_type,event_date,host_institute,position,team_size,level,date_of_award,upload_proof'
    if request.method == "POST":
        if 'columns_details' in request.POST:
            # print('type->  ',type(request.POST['columns_details']))
            columns = request.POST['columns_details'].split(',')
            # print(columns)
   
    students_data = Students.objects.values(*columns)
    # print("helloo",students_data)
    students_data_all = Students.objects.all().values()
    filter_data = {
        'Name': set(),
        'Semester':set(),
        'break1':1,
        'Departments':set(),
        'Class':set(),
        'break2':1,
        'Organized By':set(),
        'Event Name':set(),
        'break3':1,
        'Event Type':set(),
        'Host Institute':set(),
        'break4':1,
        'Position Obtained':set(),
        'Team Size':set(),
        'break5':1,
        'Level':set(),    
        'E-mail Id':set(),
        'break6':1,
        'Mobile No':set(),
        'Enrollment No':set(),
        'break7':1,
        'Award Date':set(),
        'Event Date':set(),
    }

    for student in students_data_all:
        filter_data['Name'].add(student['name'])
        filter_data['E-mail Id'].add(student['mail_id'])
        filter_data['Semester'].add(student['semester'])
        filter_data['Departments'].add(student['Departments'])
        filter_data['Class'].add(student['Class'])
        filter_data['Organized By'].add(student['organized_by'])
        filter_data['Event Name'].add(student['event_name'])
        filter_data['Event Type'].add(student['event_type'])
        filter_data['Host Institute'].add(student['host_institute'])
        filter_data['Position Obtained'].add(student['position'])
        filter_data['Team Size'].add(student['team_size'])
        filter_data['Level'].add(student['level'])
        filter_data['Event Date'].add(student['event_date'])
        filter_data['Award Date'].add(student['date_of_award'])
        filter_data['Mobile No'].add(student['mobile_no'])
        filter_data['Enrollment No'].add(student['eroll_no'])
        filter_data['E-mail Id'].add(student['mail_id'])
    
    context = {
        'fields' : fields,
        'columns' : columns,
        'students_data':students_data_all,
        'header' : 'Students',
        'display' : True,
        'columns_str':columns_str,
        'filter_data':filter_data,
    }

    if 'columns_details' in request.POST and request.POST['columns_details'] != '':
        context['columns_str'] = request.POST['columns_details']
    
    return render(request,'students/index.html',context)

# edit student entry
def edit_student_entry(request):
    id = request.POST['id_details']
    columns = request.POST['columns_details']
    # print('mansi',columns)
    # print('uff ,',type(columns))
    item = Students.objects.get(pk = id)
    form = StudentForm(instance=item)
    context = {
        'form':form,
        'columns':columns,
        'id':id
    }
    return render(request,'students/edit_students.html',context)

# saves changes and reflect in index.html file
def save_student_entry(request,pk):
    item = Students.objects.get(id =pk)
    if request.method == "POST":
        item.name = request.POST['name']
        item.eroll_no = request.POST['eroll_no']
        item.semester = request.POST['semester']
        item.Departments = request.POST['Departments']
        item.mobile_no = request.POST['mobile_no']
        item.Class = request.POST['Class']
        item.event_name = request.POST['event_name']
        item.event_type = request.POST['event_type']
        item.event_date = request.POST['event_date']
        item.organized_by = request.POST['organized_by']
        item.host_institute = request.POST['host_institute']
        item.position = request.POST['position']
        item.team_size = request.POST['team_size']
        item.level = request.POST['level']
        item.date_of_award = request.POST['date_of_award']
        upload_proof = ''
        now = datetime.now()

        if request.method == 'POST' and "upload_proof" in request.FILES and request.FILES['upload_proof']:
            upload_proof = request.FILES['upload_proof']
            fs = FileSystemStorage(location='proof/award_proof/')
            filename = fs.save(now.strftime("%H%M%S")+"_"+upload_proof.name, upload_proof)
            uploaded_file_url = fs.url(filename)
            fs.delete(item.upload_proof)
            item.upload_proof = uploaded_file_url.split('/')[-1]
            print('file changed')

    item.save()
    # print('saveed finally')
    # if 'columns_details' in request.POST:
    #     print("hello,",request.POST['columns_details'])

    return display_students_table(request)

# open the proof file 
def open_file_proof(request,file):
    return FileResponse(open('proof/award_proof/'+file, 'rb'), filename=file)

def export_data(request):
    filter_data = request.POST['filter_data']
    req_col = []
    
    if 'columns_details' in request.POST:
        req_col = request.POST['columns_details'].split(',')
        print('required cols',type(req_col))
        req_col.remove('id')

    query = Q()
    if filter_data == "All":
        query2 = Q()
    else:
        filter_data = json.loads(filter_data)
        
        name = request.POST['Name']
        semester = request.POST['Semester']
        Departments = request.POST['Departments']
        Class = request.POST['Class']
        organized_by = request.POST['Organized By']
        event_name = request.POST['Event Name']
        event_type = request.POST['Event Type']
        host_institute = request.POST['Host Institute']
        position = request.POST['Position Obtained']
        team_size = request.POST['Team Size']
        level = request.POST['Level']
        mail_id = request.POST['E-mail Id']
        eroll_no = request.POST['Enrollment No']
        mobile_no = request.POST['Mobile No']
        date_of_award = request.POST['Award Date']
        event_date = request.POST['Event Date']

        if(name != '-1'):
            query = query & Q(name = name)
        if( semester != '-1'):
            query = query & Q(semester = semester)
        if( Departments != '-1'):
            query = query & Q(Departments = Departments)
        if( Class != '-1'):
            query = query & Q(Class = Class)
        if( event_type != '-1'):
            query = query & Q(event_type = event_type)
        if( host_institute != '-1'):
            query = query & Q(host_institute = host_institute)
        if( organized_by != '-1'):
            query = query & Q(organized_by = organized_by)
        if( position != '-1'):
            query = query & Q(position = position)
        if( team_size != '-1'):
            query = query & Q(team_size = team_size)
        if( level != '-1'):
            query = query & Q(level = level)
        if( mail_id != '-1' and mail_id != ''):
            query = query & Q(mail_id = mail_id)
        if( eroll_no != '-1' and eroll_no != ''):
            query = query & Q(eroll_no = eroll_no)
        if( mobile_no != '-1' and mobile_no != ''):
            query = query & Q(mobile_no = mobile_no)
        if( event_date != '-1' and event_date != ''):
            query = query & Q(event_date = event_date)
        if( date_of_award != '-1' and date_of_award != ''):
            query = query & Q(date_of_award = date_of_award)
        
        query2 = Q()
    students_data = Students.objects.filter(query & query2).values(*req_col)
    print(students_data)
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment; filename=students.csv'
    writer = csv.writer(response)
    req_col.insert(0,'S.no')
    writer.writerow(req_col)
    writer.writerow([])
    i = 1
    for student in students_data:
        event_row = [i]
        for value in student:
            event_row.append(student[value])
            print(student[value])
        writer.writerow(event_row)
        i+=1

    return response