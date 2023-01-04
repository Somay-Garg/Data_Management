from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from manage_data.models.placementsModel import *
import json
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from django.db.models import Q
import csv
import uuid
from django.http import FileResponse

def generate_unique_id():
    return uuid.uuid4().hex[:6].upper()

def placements(request,msg=''):
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
        filter_data['Passout Year'].add(str(student['passout']).split('-')[0].split(' ')[-1])
        student['passout'] = str(student['passout']).split('-')[0].split(' ')[-1]
        filter_data['Section'].add(student['section'])

    context = {
        'fields' : fields,
        'placement_data' : placement_data,
        'header' : 'Placements',
        'filter_data' : filter_data,
        'columns':columns,
        'display':True,
        'columns_str':columns_str,
        'msg':msg,
        'showFilters':False,
    }

    if context['msg'] == 'Filters Removed.' or context['msg'] == 'Filters Added':
        context['showFilters'] = True
    
    return render(request,'placements/index.html',context)

def display_placement_columns(request,msg=''):
    fields = StudentPlacement._meta.fields
    columns = ['id','enrollmentno','name','department','section','passout']
    columns_str = 'id,enrollmentno,name,department,section,passout'
    
    if(request.method == "POST"):
        # if( 'columns_details' in request.POST and request.POST['columns_details'] != ''):
        #     columns = request.POST['columns_details'].split(',')

        if('passingColumns' in request.POST):
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
        filter_data['Passout Year'].add(str(student['passout']).split('-')[0].split(' ')[-1])
        student['passout'] = str(student['passout']).split('-')[0].split(' ')[-1]
        filter_data['Section'].add(student['section'])
    
    placement_data = ''
    if 'filter_data' in request.POST:
        filterData = request.POST['filter_data']
        query = Q()
       
        if filterData != "All":
            filterData = json.loads(filterData)
            department = filterData['Department']
            passout = filterData['Passout Year']
            section = filterData['Section']       

            if department != "-1":
                print('in dept')
                query = query & Q(department = department)
            if passout != "-1":
                query = query & Q(passout = passout +'-01-01')
            if section != "-1":
                print("in sec ")
                query = query & Q(section = section)
            
        placement_data = StudentPlacement.objects.filter(query).values(*columns)
    else:
        placement_data = placement_data_all
        
    context = {
        'fields' : fields,
        'columns' : columns,
        'placement_data' : placement_data,
        'header' : 'Placements',
        'filter_data' : filter_data,
        'display' : True,
        'columns_str':columns_str,
        'msg':'Filters Added',
        'showFilters':False,
    }

    if request.POST['show_filters'] == 'true'  or request.POST['show_filters'] == 'True' :
        context['showFilters'] = True

    # if 'columns_details' in request.POST:
    #     context['columns_str'] = request.POST['columns_details']
    if 'columns_details' not in request.POST:
        context['display'] = False
    if msg:
        context['msg'] = msg

    return render(request,'placements/index.html',context)

def filter_placement(request):
    if "resetFilter" in request.POST:
        return display_placement_columns(request,'Filters Removed.')

    if "downloadExcel" in request.POST:
        return export_placment_data(request)
    
    columns = ['id','enrollmentno','name','department','section','passout']
    # columns_str = 'id,enrollmentno,name,department,section,passout'
    if('columns_details' in request.POST and request.POST['columns_details'] != ''):
        columns = request.POST['columns_details'].split(",")

    department = request.POST['Department']
    passout = request.POST['Passout Year']
    section = request.POST['Section']

    query = Q()
    
    sel_fil_val = {
        'Department': '-1',
        'Passout Year': '-1',
        'Section': '-1',
    }

    if department != "-1":
        query = query & Q(department = department)
        sel_fil_val['Department'] = department
    if passout != "-1":
        query = query & Q(passout = passout+'-01-01')
        sel_fil_val['Passout Year'] = passout
    if section != "-1":
        query = query & Q(section = section)
        sel_fil_val['Section'] = section

    fields = StudentPlacement._meta.fields
    placement_data = StudentPlacement.objects.filter(query).values()
    all_data = StudentPlacement.objects.all().values()
    
    filter_data = {
        'Department': set(),
        'Passout Year': set(),
        'break1' : 1,
        'Section': set(),
    }

    for student in all_data:
        filter_data['Department'].add(student['department'])
        filter_data['Passout Year'].add(str(student['passout']).split('-')[0].split(' ')[-1])
        filter_data['Section'].add(student['section'])
    
    for student in placement_data:
        student['passout'] = str(student['passout']).split('-')[0].split(' ')[-1]
    
    context = {
        'fields' : fields,
        'placement_data' : placement_data,
        'header' : 'Placements',
        'filter_data' : filter_data,
        'sel_fil_val' : sel_fil_val,
        'sel_fil_val_json_string' : json.dumps(sel_fil_val),
        'columns':columns,
        'display':True,
        'msg':'Filters Added',
        'showFilters':True,
    }
    
    if('columns_details' in request.POST):
        context['columns_str'] = request.POST['columns_details']
        
    return render(request,'placements/index.html',context)

def export_placment_data(request):
    filter_data = request.POST['filter_data']
    req_col = []

    if 'columns_details' in request.POST:
        req_col = request.POST['columns_details'].split(',')
        req_col.remove('id')
    
    query = Q()

    if filter_data != "All":
        filter_data = json.loads(filter_data)
        department = filter_data['Department']
        passout = filter_data['Passout Year']
        section = filter_data['Section']

        if department != "-1":
            query = query & Q(department = department)
        if passout != "-1":
            query = query & Q(passout = passout+'-01-01')
        if section != "-1":
            query = query & Q(section = section)
        
    placement_data = StudentPlacement.objects.filter(query).values(*req_col)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=placements.csv'
    writer = csv.writer(response)
    req_col.insert(0,'S.no')
    writer.writerow(req_col)
    writer.writerow([])
    i = 1
    for placement in placement_data:
        placement_row = [i]
        for value in placement:
            try:
                if datetime.strptime(str(placement[value]), '%Y-%m-%d'):
                    placement_row.append(str(placement[value]).split('-')[0])
            except:
                placement_row.append(placement[value])
        writer.writerow(placement_row)
        i+=1

    return response

def add_placement_details(request):
    return render(request,'placements/add_placement_details.html')

def add_student_placement_detail(request):
    student_name = request.POST['student_name']
    enrollmentno = request.POST['enrollment_no']
    department = request.POST['department_name']
    section = request.POST['section']
    passout = request.POST['passout_year']+'-01-01'

    offer_detail = request.POST['offer_details']
    exam_detail = request.POST['exam_details']

    is_placed = False
    if offer_detail != '':
        is_placed = True
        offer_detail = json.loads(offer_detail)

        for key in offer_detail:
            current_offer = StudentOfferDetails()
            current_offer.enrollmentno = enrollmentno
            current_offer.company_name = offer_detail[key]['company_name']
            current_offer.package_in_lpa = offer_detail[key]['package']
            current_offer.on_off_campus = offer_detail[key]['on_off_campus']
            current_offer.job_proof = ''

            if 'upload_proof_'+key in request.FILES:
                job_proof = request.FILES['upload_proof_'+key]
                fs = FileSystemStorage(location='student_proofs/offer_proof/')
                filename = fs.save(enrollmentno+'_'+current_offer.company_name+'_'+generate_unique_id()+'.pdf', job_proof)
                uploaded_file_url = fs.url(filename)
                current_offer.job_proof = uploaded_file_url.split('/')[-1]
            current_offer.save()

    appeared_for_exams = False
    if exam_detail != '':
        appeared_for_exams = True
        exam_detail = json.loads(exam_detail)
        for key in exam_detail:
            current_exam = StudentExamDetails()
            current_exam.enrollmentno = enrollmentno
            current_exam.exam_name = exam_detail[key]['exam_name']
            current_exam.exam_roll_no = exam_detail[key]['exam_roll_no']
            current_exam.exam_date = exam_detail[key]['exam_date']
            current_exam.qualified = exam_detail[key]['qualified']
            if exam_detail[key]['exam_score'] != '':
                current_exam.score = exam_detail[key]['exam_score']
            else:
                current_exam.score = None
            if exam_detail[key]['exam_rank'] != '':
                current_exam.rank = exam_detail[key]['exam_rank']
            else:
                current_exam.rank = None
            if exam_detail[key]['date_of_result'] != '':
                current_exam.date_of_result = exam_detail[key]['date_of_result']
            else:
                current_exam.date_of_result = None

            current_exam.result_proof = None
            if 'result_proof_'+key in request.FILES:
                result_proof = request.FILES['result_proof_'+key]
                fs = FileSystemStorage(location='student_proofs/exam_proof/')
                filename = fs.save(enrollmentno+'_'+current_exam.exam_name+'_'+generate_unique_id()+'.pdf', result_proof)
                uploaded_file_url = fs.url(filename)
                current_exam.result_proof = uploaded_file_url.split('/')[-1]
            current_exam.save()

    current_status = ''
    if 'currentstatus' in request.POST:
        current_status = request.POST['currentstatus']
        if current_status == 'Job':
            job = StudentCurrentStatusJobDetails()
            job.enrollmentno = enrollmentno
            job.company_name = request.POST['job_company_name']
            job.date_of_joining = request.POST['joining_date']
            job.address = request.POST['company_address']
            
            job.job_joining_proof = ''
            if 'job_joining_proof' in request.FILES:
                job_joining_proof = request.FILES['job_joining_proof']
                fs = FileSystemStorage(location='student_proofs/current_status_proof/')
                filename = fs.save(enrollmentno+'_'+current_status+'_'+generate_unique_id()+'.pdf', job_joining_proof)
                uploaded_file_url = fs.url(filename)
                job.joining_proof = uploaded_file_url.split('/')[-1]

            job.save()
        
        elif current_status == 'Higher Education':
            high_edu = StudentCurrentStatusHighEduDetails()
            high_edu.enrollmentno = enrollmentno
            high_edu.college_name = request.POST['college_name']
            high_edu.course_name = request.POST['course_name']
            high_edu.country_name = request.POST['country']
            high_edu.college_address = request.POST['college_address']

            high_edu.college_joining_proof = ''
            if 'college_joining_proof' in request.FILES:
                college_joining_proof = request.FILES['college_joining_proof']
                fs = FileSystemStorage(location='student_proofs/current_status_proof/')
                filename = fs.save(enrollmentno+'_'+'Higher_Education'+'_'+generate_unique_id()+'.pdf', college_joining_proof)
                uploaded_file_url = fs.url(filename)
                high_edu.id_proof = uploaded_file_url.split('/')[-1]

            high_edu.save()

        elif current_status == "Entreprenurship":
            entrepre = StudentCurrentStatusEntrepreDetails()
            entrepre.enrollmentno = enrollmentno
            entrepre.startup_name = request.POST['startup_name']
            entrepre.address = request.POST['startup_company_address']
            entrepre.startup_country = request.POST['startup_country']
            entrepre.sector = request.POST['working_Sector']
            entrepre.website = request.POST['website_link']

            entrepre.save()
        
        else:
            other = request.POST['other']
            current_status = other

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

    # return redirect('placements')
    return placements(request,'Details Added')

def edit_placement_detail(request):
    id = request.POST['id_details']
    columns = request.POST['passingColumns']
    studentDetail = StudentPlacement.objects.get(pk = id)
    studentDetail.passout = str(studentDetail.passout).split('-')[0]
    studentOfferDetail = ''
    if studentDetail.is_placed:
        studentOfferDetail = StudentOfferDetails.objects.filter(enrollmentno = studentDetail.enrollmentno)
    studentExamDetail = ''
    if studentDetail.appeared_for_exams:
        studentExamDetail = StudentExamDetails.objects.filter(enrollmentno = studentDetail.enrollmentno)
        for stu in studentExamDetail:
            stu.exam_date = str(stu.exam_date)
            stu.date_of_result = str(stu.date_of_result)
            if stu.result_proof == '':
                stu.result_proof = 'none'
    current_status = studentDetail.current_status
    studentCurrentStatusDetail = ''
    if current_status == "Job":
        studentCurrentStatusDetail = StudentCurrentStatusJobDetails.objects.get(enrollmentno = studentDetail.enrollmentno)
        studentCurrentStatusDetail.date_of_joining = str(studentCurrentStatusDetail.date_of_joining)
    if current_status == "Higher Education":
        studentCurrentStatusDetail = StudentCurrentStatusHighEduDetails.objects.get(enrollmentno = studentDetail.enrollmentno)
    if current_status == "Entreprenurship":
        studentCurrentStatusDetail = StudentCurrentStatusEntrepreDetails.objects.get(enrollmentno = studentDetail.enrollmentno)
    showFilters = request.POST['show_filters']
    context = {
        'studentDetail':studentDetail,
        'studentOfferDetail':studentOfferDetail,
        'studentExamDetail':studentExamDetail,
        'studentCurrentStatusDetail':studentCurrentStatusDetail,
        'columns':columns,
        'id':id,
        'showFilters':showFilters,
    }
    return render(request,'placements/edit_placement_detail.html',context)

def save_student_placement_detail(request):
    student_name = request.POST['student_name']
    enrollmentno = request.POST['enrollment_no']
    department = request.POST['department_name']
    section = request.POST['section']
    passout = request.POST['passout_year']+'-01-01'

    # for changes in existing offers
    is_placed = False
    if request.POST['existing_offers'] != '':
        is_placed = True
        existing_offers = json.loads(request.POST['existing_offers'])
        for offer in existing_offers:
            stu = StudentOfferDetails.objects.get(id=existing_offers[offer]['offer_id'])
            stu.enrollmentno = enrollmentno
            stu.company_name = existing_offers[offer]['company_name']
            stu.package_in_lpa = existing_offers[offer]['package']
            stu.on_off_campus = existing_offers[offer]['on_off_campus']
            if 'upload_proof_'+offer in request.FILES:
                # deleting existing file
                fs = FileSystemStorage(location='student_proofs/offer_proof/')
                path = str(stu.job_proof)
                if path != "":
                    fs.delete(path)
                
                # adding new file
                job_proof = request.FILES['upload_proof_'+offer]
                fs = FileSystemStorage(location='student_proofs/offer_proof/')
                filename = fs.save(enrollmentno+'_'+stu.company_name+'_'+generate_unique_id()+'.pdf', job_proof)
                uploaded_file_url = fs.url(filename)
                stu.job_proof = uploaded_file_url.split('/')[-1]
            stu.save()

    # for deleting removed offers
    if request.POST['removed_offers'] != '':
        remove_offers = request.POST['removed_offers'].split(',')
        for offer in remove_offers:
            stu = StudentOfferDetails.objects.get(id=offer)
            fs = FileSystemStorage(location='student_proofs/offer_proof/')
            path = str(stu.job_proof)
            if path != "":
                fs.delete(path)
            StudentOfferDetails.objects.filter(id=stu.id).delete()

    # for adding new offers
    if request.POST['offer_details'] != '':
        offer_detail = request.POST['offer_details']
        if offer_detail != '':
            is_placed = True
            offer_detail = json.loads(offer_detail)

            for key in offer_detail:
                current_offer = StudentOfferDetails()
                current_offer.enrollmentno = enrollmentno
                current_offer.company_name = offer_detail[key]['company_name']
                current_offer.package_in_lpa = offer_detail[key]['package']
                current_offer.on_off_campus = offer_detail[key]['on_off_campus']
                current_offer.job_proof = ''

                if 'upload_proof_'+key in request.FILES:
                    job_proof = request.FILES['upload_proof_'+key]
                    fs = FileSystemStorage(location='student_proofs/offer_proof/')
                    filename = fs.save(enrollmentno+'_'+current_offer.company_name+'_'+generate_unique_id()+'.pdf', job_proof)
                    uploaded_file_url = fs.url(filename)
                    current_offer.job_proof = uploaded_file_url.split('/')[-1]
                current_offer.save()


    # for changes in existing exams
    appeared_for_exams = False
    if request.POST['existing_exams'] != '':
        appeared_for_exams = True
        existing_exams = json.loads(request.POST['existing_exams'])
        for exam in existing_exams:
            stu = StudentExamDetails.objects.get(id=existing_exams[exam]['exam_id'])
            stu.enrollmentno = enrollmentno
            stu.exam_name = existing_exams[exam]['exam_name']
            stu.exam_roll_no = existing_exams[exam]['exam_roll_no']
            stu.exam_date = existing_exams[exam]['exam_date']
            stu.qualified = existing_exams[exam]['qualified']
            if existing_exams[exam]['exam_score'] != '':
                stu.score = existing_exams[exam]['exam_score']
            else:
                stu.score = None
            if existing_exams[exam]['exam_rank'] != '':
                stu.rank = existing_exams[exam]['exam_rank']
            else:
                stu.rank = None
            if existing_exams[exam]['date_of_result'] != '':
                stu.date_of_result = existing_exams[exam]['date_of_result']
            else:
                stu.date_of_result = None

            # if existing_exams[exam]['qualified'] == 'not_declared':
            #     fs = FileSystemStorage(location='student_proofs/exam_proof/')
            #     path = str(stu.result_proof)
            #     if path != "":
            #         fs.delete(path)
            #     stu.result_proof = None
            if 'result_proof_'+exam in request.FILES:
                # deleting existing file
                fs = FileSystemStorage(location='student_proofs/exam_proof/')
                path = str(stu.result_proof)
                if path != "":
                    fs.delete(path)

                # adding new file
                result_proof = request.FILES['result_proof_'+exam]
                fs = FileSystemStorage(location='student_proofs/exam_proof/')
                filename = fs.save(enrollmentno+'_'+stu.exam_name+'_'+generate_unique_id()+'.pdf', result_proof)
                uploaded_file_url = fs.url(filename)
                stu.result_proof = uploaded_file_url.split('/')[-1]
            stu.save()

    # for deleting removed exams
    if request.POST['removed_exams'] != '':
        removed_exams = request.POST['removed_exams'].split(',')
        for exam in removed_exams:
            stu = StudentExamDetails.objects.get(id=exam)
            fs = FileSystemStorage(location='student_proofs/exam_proof/')
            path = str(stu.result_proof)
            if path != "":
                fs.delete(path)
            StudentExamDetails.objects.filter(id=stu.id).delete()

    # for adding new exams
    if request.POST['exam_details'] != '':
        exam_detail = request.POST['exam_details']
        if exam_detail != '':
            appeared_for_exams = True
            exam_detail = json.loads(exam_detail)
            for key in exam_detail:
                current_exam = StudentExamDetails()
                current_exam.enrollmentno = enrollmentno
                current_exam.exam_name = exam_detail[key]['exam_name']
                current_exam.exam_roll_no = exam_detail[key]['exam_roll_no']
                current_exam.exam_date = exam_detail[key]['exam_date']
                current_exam.qualified = exam_detail[key]['qualified']
                if exam_detail[key]['exam_score'] != '':
                    current_exam.score = exam_detail[key]['exam_score']
                else:
                    current_exam.score = None
                if exam_detail[key]['exam_rank'] != '':
                    current_exam.rank = exam_detail[key]['exam_rank']
                else:
                    current_exam.rank = None
                if exam_detail[key]['date_of_result'] != '':
                    current_exam.date_of_result = exam_detail[key]['date_of_result']
                else:
                    current_exam.date_of_result = None

                current_exam.result_proof = None
                if 'result_proof_'+key in request.FILES:
                    result_proof = request.FILES['result_proof_'+key]
                    fs = FileSystemStorage(location='student_proofs/exam_proof/')
                    filename = fs.save(enrollmentno+'_'+current_exam.exam_name+'_'+generate_unique_id()+'.pdf', result_proof)
                    uploaded_file_url = fs.url(filename)
                    current_exam.result_proof = uploaded_file_url.split('/')[-1]
                current_exam.save()

    student = StudentPlacement.objects.get(id=request.POST['student_id'])

    # if any changes in status
    current_status = ''
    if 'currentstatus' in request.POST:
        current_status = request.POST['currentstatus']
        status_changed = False
        # if previous status is current status with changes
        if student.current_status == request.POST['currentstatus'] and student.current_status == 'Job':
            status_changed = True
            stu = StudentCurrentStatusJobDetails.objects.get(enrollmentno=student.enrollmentno)
            stu.enrollmentno = enrollmentno
            stu.company_name = request.POST['job_company_name']
            stu.date_of_joining = request.POST['joining_date']
            stu.address = request.POST['company_address']
            if 'job_joining_proof' in request.FILES:
                fs = FileSystemStorage(location='student_proofs/current_status_proof/')
                path = str(stu.joining_proof)
                if path != "":
                    fs.delete(path)
                job_joining_proof = request.FILES['job_joining_proof']
                fs = FileSystemStorage(location='student_proofs/current_status_proof/')
                filename = fs.save(enrollmentno+'_'+student.current_status+'_'+generate_unique_id()+'.pdf', job_joining_proof)
                uploaded_file_url = fs.url(filename)
                stu.joining_proof = uploaded_file_url.split('/')[-1]
            stu.save()
        
        elif student.current_status == request.POST['currentstatus'] and student.current_status == 'Higher Education':
            status_changed = True
            stu = StudentCurrentStatusHighEduDetails.objects.get(enrollmentno=student.enrollmentno)
            stu.enrollmentno = enrollmentno
            stu.college_name = request.POST['college_name']
            stu.course_name = request.POST['course_name']
            stu.country_name = request.POST['country']
            stu.college_address = request.POST['college_address']
            if 'college_joining_proof' in request.FILES:
                fs = FileSystemStorage(location='student_proofs/current_status_proof/')
                path = str(stu.id_proof)
                if path != "":
                    fs.delete(path)
                college_joining_proof = request.FILES['college_joining_proof']
                fs = FileSystemStorage(location='student_proofs/current_status_proof/')
                filename = fs.save(enrollmentno+'_'+'Higher_Education'+'_'+generate_unique_id()+'.pdf', college_joining_proof)
                uploaded_file_url = fs.url(filename)
                stu.id_proof = uploaded_file_url.split('/')[-1]
            stu.save()

        elif student.current_status == request.POST['currentstatus'] and student.current_status == 'Entreprenurship':
            status_changed = True
            stu = StudentCurrentStatusEntrepreDetails.objects.get(enrollmentno=student.enrollmentno)
            stu.enrollmentno = enrollmentno
            stu.startup_name = request.POST['startup_name']
            stu.address = request.POST['startup_company_address']
            stu.startup_country = request.POST['startup_country']
            stu.sector = request.POST['working_Sector']
            stu.website = request.POST['website_link']
            stu.save()

        elif (student.current_status == 'entrance_exam' or student.current_status == 'jobs') and request.POST['currentstatus'] == 'Other':
            status_changed = True
            current_status = request.POST['other']

        # now the previous status will be different from current status
        # deleting previous status
        elif student.current_status == "Job":
            stu = StudentCurrentStatusJobDetails.objects.get(enrollmentno=student.enrollmentno)
            fs = FileSystemStorage(location='student_proofs/current_status_proof/')
            path = str(stu.joining_proof)
            if path != "":
                fs.delete(path)
            StudentCurrentStatusJobDetails.objects.filter(id=stu.id).delete()
        
        elif student.current_status == "Higher Education":
            stu = StudentCurrentStatusHighEduDetails.objects.get(enrollmentno=student.enrollmentno)
            fs = FileSystemStorage(location='student_proofs/current_status_proof/')
            path = str(stu.id_proof)
            if path != "":
                fs.delete(path)
            StudentCurrentStatusHighEduDetails.objects.filter(id=stu.id).delete()
        
        elif student.current_status == "Entreprenurship":
            StudentCurrentStatusEntrepreDetails.objects.filter(enrollmentno=student.enrollmentno).delete()
        
        # if old status is replaced with new one
        if not status_changed:
            if current_status == 'Job':
                job = StudentCurrentStatusJobDetails()
                job.enrollmentno = enrollmentno
                job.company_name = request.POST['job_company_name']
                job.date_of_joining = request.POST['joining_date']
                job.address = request.POST['company_address']
                
                job.job_joining_proof = ''
                if 'job_joining_proof' in request.FILES:
                    job_joining_proof = request.FILES['job_joining_proof']
                    fs = FileSystemStorage(location='student_proofs/current_status_proof/')
                    filename = fs.save(enrollmentno+'_'+current_status+'_'+generate_unique_id()+'.pdf', job_joining_proof)
                    uploaded_file_url = fs.url(filename)
                    job.joining_proof = uploaded_file_url.split('/')[-1]

                job.save()
            
            elif current_status == 'Higher Education':
                high_edu = StudentCurrentStatusHighEduDetails()
                high_edu.enrollmentno = enrollmentno
                high_edu.college_name = request.POST['college_name']
                high_edu.course_name = request.POST['course_name']
                high_edu.country_name = request.POST['country']
                high_edu.college_address = request.POST['college_address']

                high_edu.college_joining_proof = ''
                if 'college_joining_proof' in request.FILES:
                    college_joining_proof = request.FILES['college_joining_proof']
                    fs = FileSystemStorage(location='student_proofs/current_status_proof/')
                    filename = fs.save(enrollmentno+'_'+'Higher_Education'+'_'+generate_unique_id()+'.pdf', college_joining_proof)
                    uploaded_file_url = fs.url(filename)
                    high_edu.id_proof = uploaded_file_url.split('/')[-1]

                high_edu.save()

            elif current_status == "Entreprenurship":
                entrepre = StudentCurrentStatusEntrepreDetails()
                entrepre.enrollmentno = enrollmentno
                entrepre.startup_name = request.POST['startup_name']
                entrepre.address = request.POST['startup_company_address']
                entrepre.startup_country = request.POST['startup_country']
                entrepre.sector = request.POST['working_Sector']
                entrepre.website = request.POST['website_link']

                entrepre.save()
            
            else:
                other = request.POST['other']
                current_status = other
    

    student.enrollmentno = enrollmentno
    student.name = student_name
    student.department=department
    student.section=section
    student.passout=passout
    student.is_placed=is_placed
    student.appeared_for_exams=appeared_for_exams
    student.current_status=current_status
    student.save()

    return display_placement_columns(request,'Details Saved.')

def delete_placement_entry(request):
    if request.method == "POST":
        id = request.POST['id_details']
        columns = request.POST['columns_details'].split(',')
        item = get_object_or_404(StudentPlacement,pk=id)
        enrollmentno = item.enrollmentno
        # Deleting from offer section
        if item.is_placed:
            student = StudentOfferDetails.objects.filter(enrollmentno=enrollmentno)
            for stu in student:
                fs = FileSystemStorage(location='student_proofs/offer_proof/')
                path = str(stu.job_proof)
                if path != "":
                    fs.delete(path)
                StudentOfferDetails.objects.filter(id=stu.id).delete()
        
        # Deleting from exam section
        if item.appeared_for_exams:
            student = StudentExamDetails.objects.filter(enrollmentno=enrollmentno)
            for stu in student:
                fs = FileSystemStorage(location='student_proofs/exam_proof/')
                path = str(stu.result_proof)
                if path != "":
                    fs.delete(path)
                StudentExamDetails.objects.filter(id=stu.id).delete()
        
        # Deleting from current status as Job
        if item.current_status == "Job":
            student = StudentCurrentStatusJobDetails.objects.get(enrollmentno=enrollmentno)
            fs = FileSystemStorage(location='student_proofs/current_status_proof/')
            path = str(student.joining_proof)
            if path != "":
                fs.delete(path)
            StudentCurrentStatusJobDetails.objects.filter(id=student.id).delete()
        
        # Deleting from current status as Higher Education
        elif item.current_status == "Higher Education":
            student = StudentCurrentStatusHighEduDetails.objects.get(enrollmentno=enrollmentno)
            fs = FileSystemStorage(location='student_proofs/current_status_proof/')
            path = str(student.id_proof)
            print(path)
            if path != "":
                fs.delete(path)
            StudentCurrentStatusHighEduDetails.objects.filter(id=student.id).delete()
        
        # Deleting from current status as Entreprenurship
        elif item.current_status == "Entreprenurship":
            StudentCurrentStatusEntrepreDetails.objects.filter(enrollmentno=enrollmentno).delete()
        
        StudentPlacement.objects.filter(id=id).delete()
        return display_placement_columns(request,'Entry Deleted')

    else:
        return HttpResponse(True)

def show_placement_detail(request,pk,showFilters):
    id = pk
    print("mansi--->",showFilters)
    studentDetail = StudentPlacement.objects.get(pk = id)
    studentDetail.passout = str(studentDetail.passout).split('-')[0]
    studentOfferDetail = ''
    if studentDetail.is_placed:
        studentOfferDetail = StudentOfferDetails.objects.filter(enrollmentno = studentDetail.enrollmentno)
    studentExamDetail = ''
    if studentDetail.appeared_for_exams:
        studentExamDetail = StudentExamDetails.objects.filter(enrollmentno = studentDetail.enrollmentno)
        for stu in studentExamDetail:
            stu.exam_date = str(stu.exam_date)
            stu.date_of_result = str(stu.date_of_result)
    current_status = studentDetail.current_status
    studentCurrentStatusDetail = ''
    if current_status == "Job":
        studentCurrentStatusDetail = StudentCurrentStatusJobDetails.objects.get(enrollmentno = studentDetail.enrollmentno)
        studentCurrentStatusDetail.date_of_joining = str(studentCurrentStatusDetail.date_of_joining)
    if current_status == "Higher Education":
        studentCurrentStatusDetail = StudentCurrentStatusHighEduDetails.objects.get(enrollmentno = studentDetail.enrollmentno)
    if current_status == "Entreprenurship":
        studentCurrentStatusDetail = StudentCurrentStatusEntrepreDetails.objects.get(enrollmentno = studentDetail.enrollmentno)
    context = {
        'studentDetail':studentDetail,
        'studentOfferDetail':studentOfferDetail,
        'studentExamDetail':studentExamDetail,
        'studentCurrentStatusDetail':studentCurrentStatusDetail,
        'id':id,
        'showFilters':showFilters,
    }

    return render(request,'placements/show_placement_details.html',context)

def open_offer_proof(request,file):
    return FileResponse(open('student_proofs/offer_proof/'+file, 'rb'), filename=file)

def open_exam_proof(request,file):
    return FileResponse(open('student_proofs/exam_proof/'+file, 'rb'), filename=file)

def open_current_status_proof(request,file):
    return FileResponse(open('student_proofs/current_status_proof/'+file, 'rb'), filename=file)