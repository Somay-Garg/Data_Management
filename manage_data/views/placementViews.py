from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from manage_data.models.placementsModel import *
import json
from django.core.files.storage import FileSystemStorage
from datetime import datetime

def placements(request):
    fields = StudentPlacement._meta.fields
    placement_data = StudentPlacement.objects.all().values()
    columns = ['id','enrollmentno','name','department','section','passout']
    columns_str = 'id,enrollmentno,name,department,section,passout'
    filter_data = {
        'Department': set(),
        'Passout Year': set(),
        'break1' : 1,
        'Section': set(),
    }

    for student in placement_data:
        filter_data['Department'].add(student['department'])
        filter_data['Passout Year'].add(student['passout'])
        filter_data['Section'].add(student['section'])

    context = {
        'fields' : fields,
        'placement_data' : placement_data,
        'header' : 'Placements',
        'filter_data' : filter_data,
        'columns':columns,
        'display':True,
        'columns_str':columns_str,
    }

    return render(request,'placements/index.html',context)

def display_placement_columns(request):
    fields = StudentPlacement._meta.fields
    columns = ['id','enrollmentno','name','department','section','passout']
    columns_str = 'id,enrollmentno,name,department,section,passout'
    
    if(request.method == "POST"):
        if( 'columns_details' in request.POST and request.POST['columns_details'] != ''):
            print('cols_dets' , type(request.POST['columns_details']))
            columns = request.POST['columns_details'].split(',')

        elif('passingColumns' in request.POST):
            cols = request.POST['passingColumns']
            columns = json.loads(cols)
        
    placement_data = StudentPlacement.objects.values(*columns)
   
    filter_data = {
        'Department': set(),
        'Passout Year': set(),
        'break1' : 1,
        'Section': set(),
    }
    
    placement_data_all = StudentPlacement.objects.values()

    for student in placement_data_all:
        filter_data['Department'].add(student['department'])
        filter_data['Passout Year'].add(student['passout'])
        filter_data['Section'].add(student['section'])
    
    context = {
        'fields' : fields,
        'columns' : columns,
        'placement_data' : placement_data_all,
        'header' : 'Placements',
        'filter_data' : filter_data,
        'display' : True,
        'columns_str':columns_str,
    }

    if 'columns_details' in request.POST:
        context['columns_str'] = request.POST['columns_details']
    elif 'columns_details' not in request.POST:
        context['display'] = False

    return render(request,'placements/index.html',context)


def add_placement_details(request):

    return render(request,'placements/add_placement_details.html')

def add_student_placement_detail(request):
    now = datetime.now()
    student_name = request.POST['student_name']
    enrollmentno = request.POST['enrollment_no']
    department = request.POST['department_name']
    section = request.POST['section']
    # section = 'II'
    passout = request.POST['passout_year']+'-01-01'
    # passout = '2024-01-01'

    offer_detail = request.POST['offer_details']
    exam_detail = request.POST['exam_details']

    is_placed = False
    if offer_detail != '':
        is_placed = True
        offer_detail = json.loads(offer_detail)

        for key in offer_detail:
            print(offer_detail[key])
            current_offer = StudentOfferDetails()
            current_offer.enrollmentno = enrollmentno
            current_offer.company_name = offer_detail[key]['company_name']
            current_offer.package_in_lpa = offer_detail[key]['package']
            current_offer.on_off_campus = offer_detail[key]['on_off_campus']
            current_offer.job_proof = ''

            if 'upload_proof_'+key in request.FILES:
                job_proof = request.FILES['upload_proof_'+key]
                fs = FileSystemStorage(location='student_proofs/offer_proof/')
                filename = fs.save(enrollmentno+'_'+current_offer.company_name+'_'+now.strftime("%H%M%S"), job_proof)
                uploaded_file_url = fs.url(filename)
                current_offer.job_proof = uploaded_file_url.split('/')[-1]

    appeared_for_exams = False
    if exam_detail != '':
        appeared_for_exams = True
        exam_detail = json.loads(exam_detail)

        for key in exam_detail:
            print(exam_detail[key])
            current_exam = StudentExamDetails()
            current_exam.enrollmentno = enrollmentno
            current_exam.exam_name = exam_detail[key]['exam_name']
            current_exam.exam_roll_no = exam_detail[key]['exam_roll_no']
            current_exam.exam_date = exam_detail[key]['exam_date']
            current_exam.qualified = exam_detail[key]['qualified']
            current_exam.score = ''
            if exam_detail[key]['exam_score'] != 'Not Declared':
                current_exam.score = exam_detail[key]['exam_score']
            current_exam.rank = ''
            if exam_detail[key]['exam_rank'] != 'Not Declared':
                current_exam.rank = exam_detail[key]['exam_rank']

            current_exam.result_proof = ''
            if 'result_proof_'+key in request.FILES:
                result_proof = request.FILES['result_proof_'+key]
                fs = FileSystemStorage(location='student_proofs/exam_proof/')
                filename = fs.save(enrollmentno+'_'+current_exam.exam_name+'_'+now.strftime("%H%M%S"), result_proof)
                uploaded_file_url = fs.url(filename)
                current_exam.result_proof = uploaded_file_url.split('/')[-1]
            current_exam.save()

    current_status = request.POST['currentstatus']
    if current_status == 'Job':
        job = StudentCurrentStatusJobDetails()
        job.enrollmentno = enrollmentno
        company_name = request.POST['job_company_name']
        # job.company_name = request.POST['job']
        job.date_of_joining = request.POST['joining_date']
        job.address = request.POST['company_address']
        
        job.job_joining_proof = ''
        if 'job_joining_proof' in request.FILES:
            job_joining_proof = request.FILES['job_joining_proof']
            fs = FileSystemStorage(location='student_proofs/current_status_proof/')
            filename = fs.save(enrollmentno+'_'+current_status+'_'+now.strftime("%H%M%S"), job_joining_proof)
            uploaded_file_url = fs.url(filename)
            job.job_joining_proof = uploaded_file_url.split('/')[-1]
        
        # job.joining_proof = ''
        # if 'joining_proof' in request.FILES:
        #     joining_proof = request.FILES['joining_proof']
        #     fs = FileSystemStorage(location='student_proofs/current_status_proof/')
        #     filename = fs.save(enrollmentno+'_'+current_status+'_'+now.strftime("%H%M%S"), joining_proof)
        #     uploaded_file_url = fs.url(filename)
        #     job.joining_proof = uploaded_file_url.split('/')[-1]

        job.save()
    
    elif current_status == 'Higher Education' or current_status == 'high_edu':
        high_edu = StudentCurrentStatusHighEduDetails()
        high_edu.enrollmentno = enrollmentno
        high_edu.college_name = request.POST['college_name']
        high_edu.course_name = request.POST['course_name']
        high_edu.country_name = request.POST['country']

        high_edu.college_joining_proof = ''
        if 'college_joining_proof' in request.FILES:
            college_joining_proof = request.FILES['college_joining_proof']
            fs = FileSystemStorage(location='student_proofs/current_status_proof/')
            filename = fs.save(enrollmentno+'_'+current_status+'_'+now.strftime("%H%M%S"), college_joining_proof)
            uploaded_file_url = fs.url(filename)
            high_edu.college_joining_proof = uploaded_file_url.split('/')[-1]

        # high_edu.joining_proof = ''
        # if 'joining_proof' in request.FILES:
        #     joining_proof = request.FILES['joining_proof']
        #     fs = FileSystemStorage(location='student_proofs/current_status_proof/')
        #     filename = fs.save(enrollmentno+'_'+current_status+'_'+now.strftime("%H%M%S"), joining_proof)
        #     uploaded_file_url = fs.url(filename)
        #     high_edu.joining_proof = uploaded_file_url.split('/')[-1]

        high_edu.save()

    elif current_status == "Entreprenurship":
        entrepre = StudentCurrentStatusEntrepreDetails()
        entrepre.enrollmentno = enrollmentno
        entrepre.startup_name = request.POST['startup_name']
        entrepre.address = request.POST['startup_company_address']
        entrepre.sector = request.POST['working_Sector']
        entrepre.website = request.POST['website_link']

        entrepre.save()
    
    else:
        other = StudentCurrentStatusOtherDetails()
        other.enrollmentno = enrollmentno
        other.other = request.POST['other']

        other.save()

    student = StudentPlacement(
        enrollmentno = enrollmentno,
        name = student_name,
        department=department,
        section=section,
        passout=passout,
        is_placed=is_placed,
        appeared_for_exams=appeared_for_exams,
        current_status=current_status,
    )
    student.save()

    return redirect('placements')
    # return render(request,'placements/index.html')

def edit_placement_detail(request):
    return render(request,'placements/index.html')

def delete_placement_entry(request):
    return render(request,'placements/index.html')