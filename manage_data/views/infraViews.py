from operator import or_
from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from manage_data.models.infraModel import *
from ..forms import *
from django.db.models import Q
from django.http import HttpResponse
from django.http import FileResponse
from datetime import datetime
import json
import csv
from django.views.decorators.csrf import csrf_exempt


def display_infra(request,msg=''):
    fields = Infrastructure._meta.fields
    infra_data = Infrastructure.objects.all().values()
    columns=['for_year_infra_entry', 'name_of_the_institute','institute_category','name_of_affiliating_university',
    'institution_status','institute_type','year_of_establishment','year_of_1st_passout_batch','address','city','state','pincode','campus_area','total_built_up_area_in_sqmtr','total_built_up_area_in_sqft','total_playground_area','phone','email','website','head_of_the_institute','name_of_the_head_of_institution','available_courses','no_of_voluntary_programs_supported','AICTE_approved','date_of_first_AICTE_accreditation','AICTE_valid_upto','NAAC_accredited','year_of_first_NAAC_accreditation','latest_NAAC_grade','latest_NAAC_score','NAAC_accreditation_valid_upto','date_of_last_submitted_AQAR_report','ABET_accredited','NBA_accredited_courses','NBA_accreditation_valid_upto','proof_UGC_recognition','proof_yr_of_estb_of_college','latest_AICTE_renewed_approval_certificate','NBA_accreditation_certificate','NAAC_accreditation_certificate','latest_AQAR_submitted_to_NAAC','list_of_governing_body_members','list_of_academic_advisory_body','list_of_members_in_anti_ragging_committee','list_of_members_in_internal_complaint_committee','list_of_members_in_grievance_redressal_committee','list_of_members_in_disciplane_committee','list_of_members_in_ST_SC_cell','list_of_members_in_disaster_management_cell','list_of_members_in_NSS','number_of_classrooms','no_of_seminar_halls','no_of_classrooms_with_audio_visual_facility','no_of_labs','no_of_computer_labs','no_of_auditoriums','total_sitting_capacity_in_main_auditorium','no_of_conference_rooms','no_of_recreation_rooms','no_of_faculty_cabins','no_of_PCs_provided_to_student','no_of_PCs_provided_to_faculty','no_of_PCs_provided_to_other_than_faculty','total_PCs_in_campus','no_of_latest_instruments_in_labs','availability_of_water_recyling_unit','availability_of_anti_ragging_cell','availability_of_grievance_redressal_mechanism','availability_of_internal_complaints_commitee','availability_of_NSS_cell','availability_of_IQAC','availability_of_faculty_feedback_mechanism','availability_of_alumini_association','no_of_alumini','availability_of_incubation_centre','no_of_companies_setup_in_last_5_years_by_incubation_centre','hostel_facilities_for_boys','area_of_boys_hostel','capacity_of_boys_hostel','no_of_boys_in_hostel','hostel_facilities_for_girls','area_of_girls_hostel','capacity_of_girls_hostel','no_of_girls_in_hostel','no_of_students_availing_hostel_facilities','residence_facility_for_faculty','total_staff_quarters','how_many_faculties_residing_in_college_campus','no_of_faculties_visited_any_foreign_university_in_previous_AY','institute_tieup_with_foreign_university','no_of_tie_up','tieup_university_details','no_of_clubs_in_college','club_details','canteen','cricket_ground','basketball_court','football_ground','swimming_pool','lawn_tennis_court','badminton_court','bank_branch','wifi_facilities','table_tennis_boards','gymnasium','bank_ATM','no_of_publications_by_college','publication_details']

    columns_str='for_year_infra_entry,name_of_the_institute,institute_category,name_of_affiliating_university,institution_status,institute_type,year_of_establishment,year_of_1st_passout_batch,address,city,state,pincode,campus_area,total_built_up_area_in_sqmtr,total_built_up_area_in_sqft,total_playground_area,phone,email,website,head_of_the_institute,name_of_the_head_of_institution,available_courses,no_of_voluntary_programs_supported,AICTE_approved,date_of_first_AICTE_accreditation,AICTE_valid_upto,NAAC_accredited,year_of_first_NAAC_accreditation,latest_NAAC_grade,latest_NAAC_score,NAAC_accreditation_valid_upto,date_of_last_submitted_AQAR_report,ABET_accredited,NBA_accredited_courses,NBA_accreditation_valid_upto,proof_UGC_recognition,proof_yr_of_estb_of_college,latest_AICTE_renewed_approval_certificate,NBA_accreditation_certificate,NAAC_accreditation_certificate,latest_AQAR_submitted_to_NAAC,list_of_governing_body_members,list_of_academic_advisory_body,list_of_members_in_anti_ragging_committee,list_of_members_in_internal_complaint_committee,list_of_members_in_grievance_redressal_committee,list_of_members_in_disciplane_committee,list_of_members_in_ST_SC_cell,list_of_members_in_disaster_management_cell,list_of_members_in_NSS,number_of_classrooms,no_of_seminar_halls,no_of_classrooms_with_audio_visual_facility,no_of_labs,no_of_computer_labs,no_of_auditoriums,total_sitting_capacity_in_main_auditorium,no_of_conference_rooms,no_of_recreation_rooms,no_of_faculty_cabins,no_of_PCs_provided_to_student,no_of_PCs_provided_to_faculty,no_of_PCs_provided_to_other_than_faculty,total_PCs_in_campus,no_of_latest_instruments_in_labs,availability_of_water_recyling_unit,availability_of_anti_ragging_cell,availability_of_grievance_redressal_mechanism,availability_of_internal_complaints_commitee,availability_of_NSS_cell,availability_of_IQAC,availability_of_faculty_feedback_mechanism,availability_of_alumini_association,no_of_alumini,availability_of_incubation_centre,no_of_companies_setup_in_last_5_years_by_incubation_centre,hostel_facilities_for_boys,area_of_boys_hostel,capacity_of_boys_hostel,no_of_boys_in_hostel,hostel_facilities_for_girls,area_of_girls_hostel,capacity_of_girls_hostel,no_of_girls_in_hostel,no_of_students_availing_hostel_facilities,residence_facility_for_faculty,total_staff_quarters,how_many_faculties_residing_in_college_campus,no_of_faculties_visited_any_foreign_university_in_previous_AY,institute_tieup_with_foreign_university,no_of_tie_up,tieup_university_details,no_of_clubs_in_college,club_details,canteen,cricket_ground,basketball_court,football_ground,swimming_pool,lawn_tennis_court,badminton_court,bank_branch,wifi_facilities,table_tennis_boards,gymnasium,bank_ATM,no_of_publications_by_college,publication_details'

    filter_data ={
        'For Year': set()
    }
    for info in infra_data:
        filter_data['For Year'].add(info['for_year_infra_entry'])
    publication = ''
    tieup = ''
    clubTest = ''
    for info in infra_data:
        if(info['publication_details']!=''):
            publication = json.loads(info['publication_details'])
        if(info['tieup_university_details']!=''):    
            tieup = json.loads(info['tieup_university_details'])
        if(info['club_details']!=''):    
            clubTest = json.loads(info['club_details'])
    
    for info in infra_data:
        if(info['publication_details']!=''):
            info['publication_details'] = json.loads(info['publication_details'])
        if(info['tieup_university_details']!=''):    
            info['tieup_university_details'] = json.loads(info['tieup_university_details'])
        if(info['club_details']!=''):    
            info['club_details'] = json.loads(info['club_details'])
       
    context = {
        'fields' : fields,
        'infra_data' : infra_data,
        'filter_data': filter_data,
        'header' : 'Infrastructure',
        'publication' : publication,
        'tieup' :tieup,
        'clubtest' :clubTest,
        'display':True,
        'columns':columns,        
        'columns_str':columns_str,
        'msg':msg,
        'showFilters':False,
    }
     
    if context['msg'] == 'Filter removed' or context['msg'] == 'Filter Applied':
        context['showFilters'] = True 

    return render(request,'infrastructure/infraIndex.html',context)  

# display the selected columns
def display_infracolumns(request,msg=''):
    fields = Infrastructure._meta.fields
    columns=['for_year_infra_entry','name_of_the_institute','institute_category','name_of_affiliating_university',
    'institution_status','institute_type','year_of_establishment','year_of_1st_passout_batch','address','city','state','pincode','campus_area','total_built_up_area_in_sqmtr','total_built_up_area_in_sqft','total_playground_area','phone','email','website','head_of_the_institute','name_of_the_head_of_institution','available_courses','no_of_voluntary_programs_supported','AICTE_approved','date_of_first_AICTE_accreditation','AICTE_valid_upto','NAAC_accredited','year_of_first_NAAC_accreditation','latest_NAAC_grade','latest_NAAC_score','NAAC_accreditation_valid_upto','date_of_last_submitted_AQAR_report','ABET_accredited','NBA_accredited_courses','NBA_accreditation_valid_upto','proof_UGC_recognition','proof_yr_of_estb_of_college','latest_AICTE_renewed_approval_certificate','NBA_accreditation_certificate','NAAC_accreditation_certificate','latest_AQAR_submitted_to_NAAC','list_of_governing_body_members','list_of_academic_advisory_body','list_of_members_in_anti_ragging_committee','list_of_members_in_internal_complaint_committee','list_of_members_in_grievance_redressal_committee','list_of_members_in_disciplane_committee','list_of_members_in_ST_SC_cell','list_of_members_in_disaster_management_cell','list_of_members_in_NSS','number_of_classrooms','no_of_seminar_halls','no_of_classrooms_with_audio_visual_facility','no_of_labs','no_of_computer_labs','no_of_auditoriums','total_sitting_capacity_in_main_auditorium','no_of_conference_rooms','no_of_recreation_rooms','no_of_faculty_cabins','no_of_PCs_provided_to_student','no_of_PCs_provided_to_faculty','no_of_PCs_provided_to_other_than_faculty','total_PCs_in_campus','no_of_latest_instruments_in_labs','availability_of_water_recyling_unit','availability_of_anti_ragging_cell','availability_of_grievance_redressal_mechanism','availability_of_internal_complaints_commitee','availability_of_NSS_cell','availability_of_IQAC','availability_of_faculty_feedback_mechanism','availability_of_alumini_association','no_of_alumini','availability_of_incubation_centre','no_of_companies_setup_in_last_5_years_by_incubation_centre','hostel_facilities_for_boys','area_of_boys_hostel','capacity_of_boys_hostel','no_of_boys_in_hostel','hostel_facilities_for_girls','area_of_girls_hostel','capacity_of_girls_hostel','no_of_girls_in_hostel','no_of_students_availing_hostel_facilities','residence_facility_for_faculty','total_staff_quarters','how_many_faculties_residing_in_college_campus','no_of_faculties_visited_any_foreign_university_in_previous_AY','institute_tieup_with_foreign_university','no_of_tie_up','tieup_university_details','no_of_clubs_in_college','club_details','canteen','cricket_ground','basketball_court','football_ground','swimming_pool','lawn_tennis_court','badminton_court','bank_branch','wifi_facilities','table_tennis_boards','gymnasium','bank_ATM','no_of_publications_by_college','publication_details']

    columns_str='for_year_infra_entry,name_of_the_institute,institute_category,name_of_affiliating_university,institution_status,institute_type,year_of_establishment,year_of_1st_passout_batch,address,city,state,pincode,campus_area,total_built_up_area_in_sqmtr,total_built_up_area_in_sqft,total_playground_area,phone,email,website,head_of_the_institute,name_of_the_head_of_institution,available_courses,no_of_voluntary_programs_supported,AICTE_approved,date_of_first_AICTE_accreditation,AICTE_valid_upto,NAAC_accredited,year_of_first_NAAC_accreditation,latest_NAAC_grade,latest_NAAC_score,NAAC_accreditation_valid_upto,date_of_last_submitted_AQAR_report,ABET_accredited,NBA_accredited_courses,NBA_accreditation_valid_upto,proof_UGC_recognition,proof_yr_of_estb_of_college,latest_AICTE_renewed_approval_certificate,NBA_accreditation_certificate,NAAC_accreditation_certificate,latest_AQAR_submitted_to_NAAC,list_of_governing_body_members,list_of_academic_advisory_body,list_of_members_in_anti_ragging_committee,list_of_members_in_internal_complaint_committee,list_of_members_in_grievance_redressal_committee,list_of_members_in_disciplane_committee,list_of_members_in_ST_SC_cell,list_of_members_in_disaster_management_cell,list_of_members_in_NSS,number_of_classrooms,no_of_seminar_halls,no_of_classrooms_with_audio_visual_facility,no_of_labs,no_of_computer_labs,no_of_auditoriums,total_sitting_capacity_in_main_auditorium,no_of_conference_rooms,no_of_recreation_rooms,no_of_faculty_cabins,no_of_PCs_provided_to_student,no_of_PCs_provided_to_faculty,no_of_PCs_provided_to_other_than_faculty,total_PCs_in_campus,no_of_latest_instruments_in_labs,availability_of_water_recyling_unit,availability_of_anti_ragging_cell,availability_of_grievance_redressal_mechanism,availability_of_internal_complaints_commitee,availability_of_NSS_cell,availability_of_IQAC,availability_of_faculty_feedback_mechanism,availability_of_alumini_association,no_of_alumini,availability_of_incubation_centre,no_of_companies_setup_in_last_5_years_by_incubation_centre,hostel_facilities_for_boys,area_of_boys_hostel,capacity_of_boys_hostel,no_of_boys_in_hostel,hostel_facilities_for_girls,area_of_girls_hostel,capacity_of_girls_hostel,no_of_girls_in_hostel,no_of_students_availing_hostel_facilities,residence_facility_for_faculty,total_staff_quarters,how_many_faculties_residing_in_college_campus,no_of_faculties_visited_any_foreign_university_in_previous_AY,institute_tieup_with_foreign_university,no_of_tie_up,tieup_university_details,no_of_clubs_in_college,club_details,canteen,cricket_ground,basketball_court,football_ground,swimming_pool,lawn_tennis_court,badminton_court,bank_branch,wifi_facilities,table_tennis_boards,gymnasium,bank_ATM,no_of_publications_by_college,publication_details'

    
    infra_data_all = Infrastructure.objects.values()
    filter_data ={
        'For Year': set()
    }
    for info in infra_data_all:
        filter_data['For Year'].add(info['for_year_infra_entry'])
    
    publication = ''
    tieup = ''
    clubtest = ''
    for info in infra_data_all:
        if(info['publication_details']!=''):
            publication = json.loads(info['publication_details'])
        if(info['tieup_university_details']!=''):    
            tieup = json.loads(info['tieup_university_details'])
        if(info['club_details']!=''):    
            clubTest = json.loads(info['club_details'])
    
    for info in infra_data_all:
        if(info['publication_details']!=''):
            info['publication_details'] = json.loads(info['publication_details'])
        if(info['tieup_university_details']!=''):    
            info['tieup_university_details'] = json.loads(info['tieup_university_details'])
        if(info['club_details']!=''):    
            info['club_details'] = json.loads(info['club_details'])

    infra_data=''
    if 'filter_data' in request.POST:
        filterData = request.POST['filter_data']
        query = Q()
        if filterData == "All" :
            query2 = Q()
        elif 'resetFilter' in request.POST and request.POST['resetFilter'] == 'reset':
            query2 = Q()   
        else:
            filterData = json.loads(filterData)
            for_year_infra_entry = filterData['For Year']

            if( for_year_infra_entry != '-1' and for_year_infra_entry != ''):
                query = query & Q(for_year_infra_entry = for_year_infra_entry)    

        infra_data = Infrastructure.objects.filter(query).order_by('for_year_infra_entry').values(*columns)
    else:
        infra_data=infra_data_all

    context = {
        'fields' : fields,
        'columns' : columns,
        'infra_data' : infra_data,
        'header' : 'Infrastructure',
        'columns_str': columns_str,
        'filter_data':filter_data,
        'publications' : publication,
        'tieup' : tieup,
        'clubtest' : clubtest,
        'msg':msg,
        'showFilter':False,
        'display' : True,
        
    }
    
    if request.POST['show_filters'] == 'true'  or request.POST['show_filters'] == 'True' :
        context['showFilters'] = True 

    return render(request,'infrastructure/infraIndex.html',context)

# add new entry
def add_infra(request):

    if request.method == "POST":
        now=datetime.now()
        for_year_infra_entry = request.POST['for_year_infra_entry']
        name_of_the_institute = request.POST['name_of_the_institute']
        institute_category = request.POST['institute_category']
        name_of_affiliating_university = request.POST['name_of_affiliating_university']
        institution_status = request.POST['institution_status']
        institute_type = request.POST['institute_type']
        year_of_establishment = request.POST['yr_of_establishment']
        year_of_1st_passout_batch = request.POST['yr_of_1st_passout_batch']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        pincode = request.POST['pincode']
        campus_area = request.POST['campus_area']
        total_built_up_area_in_sqmtr = request.POST['total_built_up_area_in_sqmtr']
        total_built_up_area_in_sqft = request.POST['total_built_up_area_in_sqft']
        total_playground_area = request.POST['total_playground_area']
        phone = request.POST['phone']
        email = request.POST['email']
        website = request.POST['website']
        head_of_the_institute = request.POST['head_of_the_institute']
        name_of_the_head_of_institution = request.POST['name_of_the_head_of_institution']
        available_courses = request.POST['available_courses']
        no_of_voluntary_programs_supported = request.POST['no_of_voluntary_programs_supported']
        AICTE_approved = request.POST['AICTE_approved']
        date_of_first_AICTE_accreditation = request.POST['date_of_first_AICTE_accreditation']
        AICTE_valid_upto = request.POST['AICTE_valid_upto_yr']
        NAAC_accredited = request.POST['NAAC_accredited']
        year_of_first_NAAC_accreditation = request.POST['yr_of_first_NAAC_accreditation']
        latest_NAAC_grade=request.POST['latest_NAAC_grade']
        latest_NAAC_score=request.POST['latest_NAAC_score']
        NAAC_accreditation_valid_upto=request.POST['NAAC_accreditation_valid_upto_yr']
        date_of_last_submitted_AQAR_report=request.POST['date_of_last_submitted_AQAR_report']
        ABET_accredited=request.POST['ABET_accredited']
        NBA_accredited_courses=request.POST['NBA_accredited_courses']
        NBA_accreditation_valid_upto=request.POST['NBA_accreditation_valid_upto_yr']
        proof_UGC_recognition=''
        proof_yr_of_estb_of_college=''
        latest_AICTE_renewed_approval_certificate=''
        NBA_accreditation_certificate=''
        NAAC_accreditation_certificate=''
        latest_AQAR_submitted_to_NAAC=''
        list_of_governing_body_members=''
        list_of_academic_advisory_body=''
        list_of_members_in_anti_ragging_committee=''
        list_of_members_in_internal_complaint_committee=''
        list_of_members_in_grievance_redressal_committee=''
        list_of_members_in_disciplane_committee=''
        list_of_members_in_ST_SC_cell=''
        list_of_members_in_disaster_management_cell=''
        list_of_members_in_NSS=''
        number_of_classrooms=request.POST['number_of_classrooms']
        no_of_seminar_halls = request.POST['no_of_seminar_halls']
        no_of_classrooms_with_audio_visual_facility=request.POST['no_of_classrooms_with_audio_visual_facility']
        no_of_labs=request.POST['no_of_labs']
        no_of_computer_labs=request.POST['no_of_computer_labs']
        no_of_auditoriums=request.POST['no_of_auditoriums']
        total_sitting_capacity_in_main_auditorium=request.POST['total_sitting_capacity_in_main_auditorium']
        no_of_conference_rooms=request.POST['no_of_conference_rooms']
        no_of_recreation_rooms=request.POST['no_of_recreation_rooms']
        no_of_faculty_cabins=request.POST['no_of_faculty_cabins']
        no_of_PCs_provided_to_student=request.POST['no_of_PCs_provided_to_student']
        no_of_PCs_provided_to_faculty = request.POST['no_of_PCs_provided_to_faculty']
        no_of_PCs_provided_to_other_than_faculty=request.POST['no_of_PCs_provided_to_other_than_faculty']
        total_PCs_in_campus=request.POST['total_PCs_in_campus']
        no_of_latest_instruments_in_labs=request.POST['no_of_latest_instruments_in_labs']
        availability_of_water_recyling_unit=request.POST['availability_of_water_recyling_unit']
        availability_of_anti_ragging_cell=request.POST['availability_of_anti_ragging_cell']
        availability_of_grievance_redressal_mechanism=request.POST['availability_of_grievance_redressal_mechanism']
        availability_of_internal_complaints_commitee=request.POST['availability_of_internal_complaints_commitee']
        availability_of_NSS_cell=request.POST['availability_of_NSS_cell']
        availability_of_IQAC=request.POST['availability_of_IQAC']
        availability_of_faculty_feedback_mechanism=request.POST['availability_of_faculty_feedback_mechanism']
        availability_of_alumini_association=request.POST['availability_of_alumini_association']
        no_of_alumini=request.POST['no_of_alumini']
        availability_of_incubation_centre=request.POST['availability_of_incubation_centre']
        no_of_companies_setup_in_last_5_years_by_incubation_centre=request.POST['no_of_companies_setup_in_last_5_years_by_incubation_centre']
        hostel_facilities_for_boys=request.POST['hostel_facilities_for_boys']
        area_of_boys_hostel=request.POST['area_of_boys_hostel']
        capacity_of_boys_hostel=request.POST['capacity_of_boys_hostel']
        no_of_boys_in_hostel=request.POST['no_of_boys_in_hostel']
        hostel_facilities_for_girls=request.POST['hostel_facilities_for_girls']
        area_of_girls_hostel=request.POST['area_of_girls_hostel']
        capacity_of_girls_hostel=request.POST['capacity_of_girls_hostel']
        no_of_girls_in_hostel=request.POST['no_of_girls_in_hostel']
        no_of_students_availing_hostel_facilities=request.POST['no_of_students_availing_hostel_facilities']
        residence_facility_for_faculty=request.POST['residence_facility_for_faculty']
        total_staff_quarters=request.POST['total_staff_quarters']
        how_many_faculties_residing_in_college_campus=request.POST['how_many_faculties_residing_in_college_campus']
        no_of_faculties_visited_any_foreign_university_in_previous_AY=request.POST['no_of_faculties_visited_any_foreign_university_in_previous_AY']
        institute_tieup_with_foreign_university=request.POST['institute_tieup_with_foreign_university']
        no_of_tie_up=request.POST['no_of_tie_up']

        if(request.POST['tieup_university_details']!=''):
            tieup_university_details=json.loads(request.POST['tieup_university_details'])
            for key in tieup_university_details:
                if request.method == 'POST' and request.FILES['tieup_MoU_proof_'+key]:
                    tieup_MoU_proof =request.FILES['tieup_MoU_proof_'+key]
                    fs = FileSystemStorage(location='infra_files/Mou_proof/')
                    filename = fs.save(now.strftime("%H%M%S")+'_'+key+".pdf", tieup_MoU_proof)
                    uploaded_file_url = fs.url(filename)
                    tieup_university_details[key]['tieup_MoU_proof'] = uploaded_file_url.split('/')[-1]  
            tieup_university_details=json.dumps(tieup_university_details)        
        no_of_clubs_in_college=request.POST['no_of_clubs_in_college']
        club_details=request.POST['club_details']
        canteen=request.POST['canteen']
        cricket_ground=request.POST['cricket_ground']
        basketball_court=request.POST['basketball_court']
        football_ground=request.POST['football_ground']
        swimming_pool=request.POST['swimming_pool']
        lawn_tennis_court=request.POST['lawn_tennis_court']
        badminton_court=request.POST['badminton_court']
        bank_branch=request.POST['bank_branch']
        wifi_facilities=request.POST['wifi_facilities']
        table_tennis_boards=request.POST['table_tennis_boards']
        gymnasium=request.POST['gymnasium']
        bank_ATM=request.POST['bank_ATM']
        no_of_publications_by_college=request.POST['no_of_publications_by_college']
        publication_details=request.POST['publication_details'] 
        

        if request.method == 'POST' and request.FILES['proof_UGC_recognition']:
            proof_UGC_recognition = request.FILES['proof_UGC_recognition']
            fs = FileSystemStorage(location='infra_files/UGC_proof/')
            filename = fs.save(now.strftime("%H%M%S")+".pdf", proof_UGC_recognition)
            uploaded_file_url = fs.url(filename)
            proof_UGC_recognition = uploaded_file_url.split('/')[-1]

        if request.method == 'POST' and request.FILES['proof_yr_of_estb_of_college']:
            proof_yr_of_estb_of_college = request.FILES['proof_yr_of_estb_of_college']
            fs = FileSystemStorage(location='infra_files/college_estb_proof/')
            filename = fs.save(now.strftime("%H%M%S")+".pdf", proof_yr_of_estb_of_college)
            uploaded_file_url = fs.url(filename)
            proof_yr_of_estb_of_college = uploaded_file_url.split('/')[-1]    

        if request.method == 'POST' and request.FILES['latest_AICTE_renewed_approval_certificate']:
            latest_AICTE_renewed_approval_certificate = request.FILES['latest_AICTE_renewed_approval_certificate']
            fs = FileSystemStorage(location='infra_files/AICTE_renew_proof/')
            filename = fs.save(now.strftime("%H%M%S")+".pdf", latest_AICTE_renewed_approval_certificate)
            uploaded_file_url = fs.url(filename)
            latest_AICTE_renewed_approval_certificate = uploaded_file_url.split('/')[-1]

        if request.method == 'POST' and request.FILES['NBA_accreditation_certificate']:
            NBA_accreditation_certificate = request.FILES['NBA_accreditation_certificate']
            fs = FileSystemStorage(location='infra_files/NBA_accr_proof/')
            filename = fs.save(now.strftime("%H%M%S")+".pdf", NBA_accreditation_certificate)
            uploaded_file_url = fs.url(filename)
            NBA_accreditation_certificate = uploaded_file_url.split('/')[-1] 

        if request.method == 'POST' and request.FILES['NAAC_accreditation_certificate']:
            NAAC_accreditation_certificate = request.FILES['NAAC_accreditation_certificate']
            fs = FileSystemStorage(location='infra_files/NAAC_accr_proof/')
            filename = fs.save(now.strftime("%H%M%S")+".pdf", NAAC_accreditation_certificate)
            uploaded_file_url = fs.url(filename)
            NAAC_accreditation_certificate = uploaded_file_url.split('/')[-1]  

        if request.method == 'POST' and request.FILES['latest_AQAR_submitted_to_NAAC']:
            latest_AQAR_submitted_to_NAAC = request.FILES['latest_AQAR_submitted_to_NAAC']
            fs = FileSystemStorage(location='infra_files/AQAR_proof/')
            filename = fs.save(now.strftime("%H%M%S")+".pdf", latest_AQAR_submitted_to_NAAC)
            uploaded_file_url = fs.url(filename)
            latest_AQAR_submitted_to_NAAC = uploaded_file_url.split('/')[-1] 

        if request.method == 'POST' and request.FILES['list_of_governing_body_members']:
            list_of_governing_body_members = request.FILES['list_of_governing_body_members']
            fs = FileSystemStorage(location='infra_files/governing_list/')
            filename = fs.save(now.strftime("%H%M%S")+".pdf", list_of_governing_body_members)
            uploaded_file_url = fs.url(filename)
            list_of_governing_body_members = uploaded_file_url.split('/')[-1]

        if request.method == 'POST' and request.FILES['list_of_academic_advisory_body']:
            list_of_academic_advisory_body = request.FILES['list_of_academic_advisory_body']
            fs = FileSystemStorage(location='infra_files/academic_list/')
            filename = fs.save(now.strftime("%H%M%S")+".pdf", list_of_academic_advisory_body)
            uploaded_file_url = fs.url(filename)
            list_of_academic_advisory_body = uploaded_file_url.split('/')[-1]  

        if request.method == 'POST' and request.FILES['list_of_members_in_anti_ragging_committee']:
            list_of_members_in_anti_ragging_committee = request.FILES['list_of_members_in_anti_ragging_committee']
            fs = FileSystemStorage(location='infra_files/anti_rag_list/')
            filename = fs.save(now.strftime("%H%M%S")+".pdf", list_of_members_in_anti_ragging_committee)
            uploaded_file_url = fs.url(filename)
            list_of_members_in_anti_ragging_committee = uploaded_file_url.split('/')[-1]                  

        if request.method == 'POST' and request.FILES['list_of_members_in_internal_complaint_committee']:
            list_of_members_in_internal_complaint_committee = request.FILES['list_of_members_in_internal_complaint_committee']
            fs = FileSystemStorage(location='infra_files/int_complain_list/')
            filename = fs.save(now.strftime("%H%M%S")+".pdf", list_of_members_in_internal_complaint_committee)
            uploaded_file_url = fs.url(filename)
            list_of_members_in_internal_complaint_committee = uploaded_file_url.split('/')[-1] 

        if request.method == 'POST' and request.FILES['list_of_members_in_grievance_redressal_committee']:
            list_of_members_in_grievance_redressal_committee = request.FILES['list_of_members_in_grievance_redressal_committee']
            fs = FileSystemStorage(location='infra_files/grievance_list/')
            filename = fs.save(now.strftime("%H%M%S")+".pdf", list_of_members_in_grievance_redressal_committee)
            uploaded_file_url = fs.url(filename)
            list_of_members_in_grievance_redressal_committee = uploaded_file_url.split('/')[-1]       

        if request.method == 'POST' and request.FILES['list_of_members_in_disciplane_committee']:
            list_of_members_in_disciplane_committee = request.FILES['list_of_members_in_disciplane_committee']
            fs = FileSystemStorage(location='infra_files/disciplane_list/')
            filename = fs.save(now.strftime("%H%M%S")+".pdf", list_of_members_in_disciplane_committee)
            uploaded_file_url = fs.url(filename)
            list_of_members_in_disciplane_committee = uploaded_file_url.split('/')[-1]   

        if request.method == 'POST' and request.FILES['list_of_members_in_ST_SC_cell']:
            list_of_members_in_ST_SC_cell = request.FILES['list_of_members_in_ST_SC_cell']
            fs = FileSystemStorage(location='infra_files/ST_SC_list/')
            filename = fs.save(now.strftime("%H%M%S")+".pdf", list_of_members_in_ST_SC_cell)
            uploaded_file_url = fs.url(filename)
            list_of_members_in_ST_SC_cell = uploaded_file_url.split('/')[-1] 

        if request.method == 'POST' and request.FILES['list_of_members_in_disaster_management_cell']:
            list_of_members_in_disaster_management_cell = request.FILES['list_of_members_in_disaster_management_cell']
            fs = FileSystemStorage(location='infra_files/disaster_mng_list/')
            filename = fs.save(now.strftime("%H%M%S")+".pdf", list_of_members_in_disaster_management_cell)
            uploaded_file_url = fs.url(filename)
            list_of_members_in_disaster_management_cell = uploaded_file_url.split('/')[-1] 

        if request.method == 'POST' and request.FILES['list_of_members_in_NSS']:
            list_of_members_in_NSS = request.FILES['list_of_members_in_NSS']
            fs = FileSystemStorage(location='infra_files/NSS_list/')
            filename = fs.save(now.strftime("%H%M%S")+".pdf", list_of_members_in_NSS)
            uploaded_file_url = fs.url(filename)
            list_of_members_in_NSS = uploaded_file_url.split('/')[-1]           

        infra = Infrastructure()
        infra.for_year_infra_entry=for_year_infra_entry
        infra.name_of_the_institute=name_of_the_institute
        infra.institute_category=institute_category
        infra.name_of_affiliating_university=name_of_affiliating_university
        infra.institution_status=institution_status
        infra.institute_type=institute_type
        infra.year_of_establishment=year_of_establishment
        infra.year_of_1st_passout_batch=year_of_1st_passout_batch
        infra.address=address
        infra.city=city
        infra.state=state
        infra.pincode=pincode
        infra.campus_area=campus_area
        infra.total_built_up_area_in_sqmtr=total_built_up_area_in_sqmtr
        infra.total_built_up_area_in_sqft=total_built_up_area_in_sqft
        infra.total_playground_area=total_playground_area
        infra.phone=phone
        infra.email=email
        infra.website=website
        infra.head_of_the_institute=head_of_the_institute
        infra.name_of_the_head_of_institution=name_of_the_head_of_institution
        infra.available_courses= available_courses
        infra.no_of_voluntary_programs_supported=no_of_voluntary_programs_supported
        infra.AICTE_approved=AICTE_approved
        infra.date_of_first_AICTE_accreditation=date_of_first_AICTE_accreditation
        infra.AICTE_valid_upto=AICTE_valid_upto
        infra.NAAC_accredited=NAAC_accredited
        infra.year_of_first_NAAC_accreditation=year_of_first_NAAC_accreditation
        infra.latest_NAAC_grade=latest_NAAC_grade
        infra.latest_NAAC_score=latest_NAAC_score
        infra.NAAC_accreditation_valid_upto=NAAC_accreditation_valid_upto
        infra.date_of_last_submitted_AQAR_report=date_of_last_submitted_AQAR_report
        infra.ABET_accredited=ABET_accredited
        infra.NBA_accredited_courses=NBA_accredited_courses
        infra.NBA_accreditation_valid_upto=NBA_accreditation_valid_upto
        infra.proof_UGC_recognition=proof_UGC_recognition
        infra.proof_yr_of_estb_of_college=proof_yr_of_estb_of_college
        infra.latest_AICTE_renewed_approval_certificate=latest_AICTE_renewed_approval_certificate
        infra.NBA_accreditation_certificate=NBA_accreditation_certificate
        infra.NAAC_accreditation_certificate=NAAC_accreditation_certificate
        infra.latest_AQAR_submitted_to_NAAC=latest_AQAR_submitted_to_NAAC
        infra.list_of_governing_body_members=list_of_governing_body_members
        infra.list_of_academic_advisory_body=list_of_academic_advisory_body
        infra.list_of_members_in_anti_ragging_committee=list_of_members_in_anti_ragging_committee
        infra.list_of_members_in_internal_complaint_committee=list_of_members_in_internal_complaint_committee
        infra.list_of_members_in_grievance_redressal_committee=list_of_members_in_grievance_redressal_committee
        infra.list_of_members_in_disciplane_committee=list_of_members_in_disciplane_committee
        infra.list_of_members_in_ST_SC_cell=list_of_members_in_ST_SC_cell
        infra.list_of_members_in_disaster_management_cell=list_of_members_in_disaster_management_cell
        infra.list_of_members_in_NSS=list_of_members_in_NSS
        infra.number_of_classrooms=number_of_classrooms
        infra.no_of_seminar_halls=no_of_seminar_halls
        infra.no_of_classrooms_with_audio_visual_facility=no_of_classrooms_with_audio_visual_facility
        infra.no_of_labs=no_of_labs
        infra.no_of_computer_labs=no_of_computer_labs
        infra.no_of_auditoriums=no_of_auditoriums
        infra.total_sitting_capacity_in_main_auditorium=total_sitting_capacity_in_main_auditorium
        infra.no_of_conference_rooms=no_of_conference_rooms
        infra.no_of_recreation_rooms=no_of_recreation_rooms
        infra.no_of_faculty_cabins=no_of_faculty_cabins
        infra.no_of_PCs_provided_to_student=no_of_PCs_provided_to_student
        infra.no_of_PCs_provided_to_faculty=no_of_PCs_provided_to_faculty
        infra.no_of_PCs_provided_to_other_than_faculty=no_of_PCs_provided_to_other_than_faculty
        infra.total_PCs_in_campus=total_PCs_in_campus
        infra.no_of_latest_instruments_in_labs=no_of_latest_instruments_in_labs
        infra.availability_of_water_recyling_unit=availability_of_water_recyling_unit
        infra.availability_of_anti_ragging_cell=availability_of_anti_ragging_cell
        infra.availability_of_grievance_redressal_mechanism=availability_of_grievance_redressal_mechanism
        infra.availability_of_internal_complaints_commitee=availability_of_internal_complaints_commitee
        infra.availability_of_NSS_cell=availability_of_NSS_cell
        infra.availability_of_IQAC=availability_of_IQAC
        infra.availability_of_faculty_feedback_mechanism=availability_of_faculty_feedback_mechanism
        infra.availability_of_alumini_association=availability_of_alumini_association
        infra.no_of_alumini=no_of_alumini
        infra.availability_of_incubation_centre=availability_of_incubation_centre
        infra.no_of_companies_setup_in_last_5_years_by_incubation_centre=no_of_companies_setup_in_last_5_years_by_incubation_centre
        infra.hostel_facilities_for_boys=hostel_facilities_for_boys
        infra.area_of_boys_hostel=area_of_boys_hostel
        infra.capacity_of_boys_hostel=capacity_of_boys_hostel
        infra.no_of_boys_in_hostel=no_of_boys_in_hostel
        infra.hostel_facilities_for_girls=hostel_facilities_for_girls
        infra.area_of_girls_hostel=area_of_girls_hostel
        infra.capacity_of_girls_hostel=capacity_of_girls_hostel
        infra.no_of_girls_in_hostel=no_of_girls_in_hostel
        infra.no_of_students_availing_hostel_facilities=no_of_students_availing_hostel_facilities
        infra.residence_facility_for_faculty=residence_facility_for_faculty
        infra.total_staff_quarters=total_staff_quarters
        infra.how_many_faculties_residing_in_college_campus=how_many_faculties_residing_in_college_campus
        infra.no_of_faculties_visited_any_foreign_university_in_previous_AY=no_of_faculties_visited_any_foreign_university_in_previous_AY
        infra.institute_tieup_with_foreign_university=institute_tieup_with_foreign_university
        if(no_of_tie_up!=''):
            infra.no_of_tie_up=no_of_tie_up
        infra.tieup_university_details=tieup_university_details
        infra.club_details=club_details
        infra.no_of_clubs_in_college=no_of_clubs_in_college
        infra.canteen=canteen
        infra.cricket_ground=cricket_ground
        infra.basketball_court=basketball_court
        infra.football_ground=football_ground
        infra.swimming_pool=swimming_pool
        infra.lawn_tennis_court=lawn_tennis_court
        infra.badminton_court=badminton_court
        infra.bank_branch=bank_branch
        infra.wifi_facilities=wifi_facilities
        infra.table_tennis_boards=table_tennis_boards
        infra.gymnasium=gymnasium
        infra.bank_ATM=bank_ATM
        infra.no_of_publications_by_college=no_of_publications_by_college
        infra.publication_details=publication_details
        infra.save()
        return display_infra(request,'Details Added')
    else:
        return render(request,'infrastructure/addInfra.html',{})    

# filter event data
def filter_infra(request):
    if request.method == 'POST':
        if "resetFilter" in request.POST:
            return display_infracolumns(request,'Filter removed')
        if "downloadExcel" in request.POST:
            return export_data(request)   

        columns=['for_year_infra_entry','name_of_the_institute','institute_category','name_of_affiliating_university','institution_status','institute_type','year_of_establishment','year_of_1st_passout_batch','address','city','state','pincode','campus_area','total_built_up_area_in_sqmtr','total_built_up_area_in_sqft','total_playground_area','phone','email','website','head_of_the_institute','name_of_the_head_of_institution','available_courses','no_of_voluntary_programs_supported','AICTE_approved','year_of_first_AICTE_accreditation','AICTE_valid_upto','NAAC_accredited','year_of_first_NAAC_accreditation','latest_NAAC_grade','latest_NAAC_score','NAAC_accreditation_valid_upto','date_of_last_submitted_AQAR_report','ABET_accredited','NBA_accredited_courses','NBA_accreditation_valid_upto','proof_UGC_recognition','proof_yr_of_estb_of_college','latest_AICTE_renewed_approval_certificate','NBA_accreditation_certificate','NAAC_accreditation_certificate','latest_AQAR_submitted_to_NAAC','list_of_governing_body_members','list_of_academic_advisory_body','list_of_members_in_anti_ragging_committee','list_of_members_in_internal_complaint_committee','list_of_members_in_grievance_redressal_committee','list_of_members_in_disciplane_committee','list_of_members_in_ST_SC_cell','list_of_members_in_disaster_management_cell','list_of_members_in_NSS','number_of_classrooms','no_of_seminar_halls','no_of_classrooms_with_audio_visual_facility','no_of_labs','no_of_computer_labs','no_of_auditoriums','total_sitting_capacity_in_main_auditorium','no_of_conference_rooms','no_of_recreation_rooms','no_of_faculty_cabins','no_of_PCs_provided_to_student','no_of_PCs_provided_to_faculty','no_of_PCs_provided_to_other_than_faculty','total_PCs_in_campus','no_of_latest_instruments_in_labs','availability_of_water_recyling_unit','availability_of_anti_ragging_cell','availability_of_grievance_redressal_mechanism','availability_of_internal_complaints_commitee','availability_of_NSS_cell','availability_of_IQAC','availability_of_faculty_feedback_mechanism','availability_of_alumini_association','no_of_alumini','availability_of_incubation_centre','no_of_companies_setup_in_last_5_years_by_incubation_centre','hostel_facilities_for_boys','area_of_boys_hostel','capacity_of_boys_hostel','no_of_boys_in_hostel','hostel_facilities_for_girls','area_of_girls_hostel','capacity_of_girls_hostel','no_of_girls_in_hostel','no_of_students_availing_hostel_facilities','residence_facility_for_faculty','total_staff_quarters','how_many_faculties_residing_in_college_campus','no_of_faculties_visited_any_foreign_university_in_previous_AY','institute_tieup_with_foreign_university','no_of_tie_up','tieup_university_details','no_of_clubs_in_college','club_details','canteen','cricket_ground','basketball_court','football_ground','swimming_pool','lawn_tennis_court','badminton_court','bank_branch','wifi_facilities','table_tennis_boards','gymnasium','bank_ATM','no_of_publications_by_college','publication_details']
        if('columns_details' in request.POST and request.POST['columns_details'] != ''):
            columns = request.POST['columns_details'].split(",")

        for_year_infra_entry = request.POST['For Year']

        infra_data_all = Infrastructure.objects.all().values()
        filter_data = {
        'For Year' : set()
        }
    
    publication = ''
    for info in infra_data_all:
        filter_data['For Year'].add(info['for_year_infra_entry'])

        query = Q()
        
        sel_fil_val = {
            'For Year' : '-1'
        }

        if(for_year_infra_entry != "-1"):
            query = query & Q(for_year_infra_entry = for_year_infra_entry)
            sel_fil_val['For Year'] = for_year_infra_entry
        
             
    
        fields = Infrastructure._meta.fields
        
        infra_data = Infrastructure.objects.filter(query).values()
        
        context = {
            'fields' : fields,
            'infra_data' : infra_data,
            'header' : 'Infrastructure',
            'filter_data' : filter_data,
            'sel_fil_val' : sel_fil_val,
            'publications' : publication,
            'sel_fil_val_json_string' : json.dumps(sel_fil_val),
            'columns':columns,
            'display':True,
            'msg': 'Filter Applied',
            'showFilters':True,
        }
        
        if('columns_details' in request.POST and request.POST['columns_details'] != ''):
            context['columns_str'] = request.POST['columns_details']
               
        return render(request,'Infrastructure/infraIndex.html',context)
    else:
        return render(request,'Infrastructure/addInfra.html',{})        

def delete_infra_entry(request):
    if request.method == "POST":
        id = request.POST['id_details']
        columns = request.POST['columns_details'].split(',')
        item = get_object_or_404(Infrastructure,pk=id)
        fs_ugc = FileSystemStorage(location='infra_files/UGC_proof/')
        path_ugc = str(item.proof_UGC_recognition)
        if path_ugc != '':
         fs_ugc.delete(path_ugc)
        fs_estb = FileSystemStorage(location='infra_files/college_estb_proof/')
        path_college_estb = str(item.proof_yr_of_estb_of_college)
        fs_estb.delete(path_college_estb)
        fs_AICTE = FileSystemStorage(location='infra_files/AICTE_renew_proof')
        path_AICTE=str(item.latest_AICTE_renewed_approval_certificate)
        fs_AICTE.delete(path_AICTE)
        fs_NBA = FileSystemStorage(location='infra_files/NBA_accr_proof')
        path_NBA=str(item.NBA_accreditation_certificate)
        fs_NBA.delete(path_NBA)
        fs_NAAC = FileSystemStorage(location='infra_files/NAAC_accr_proof')
        path_NAAC=str(item.NAAC_accreditation_certificate)
        fs_NAAC.delete(path_NAAC)
        fs_AQAR = FileSystemStorage(location='infra_files/AQAR_proof')
        path_AQAR=str(item.latest_AQAR_submitted_to_NAAC)
        fs_AQAR.delete(path_AQAR)
        fs_gov = FileSystemStorage(location='infra_files/governing_list')
        path_gov=str(item.list_of_governing_body_members)
        fs_gov.delete(path_gov)
        fs_academic = FileSystemStorage(location='infra_files/academic_list')
        path_academic=str(item.list_of_academic_advisory_body)
        fs_academic.delete(path_academic)
        fs_anti_rag = FileSystemStorage(location='infra_files/anti_rag_list')
        path_anti_rag=str(item.list_of_members_in_anti_ragging_committee)
        fs_anti_rag.delete(path_anti_rag)
        fs_int_complain = FileSystemStorage(location='infra_files/int_complain_list')
        path_int_complaint=str(item.list_of_members_in_internal_complaint_committee)
        fs_int_complain.delete(path_int_complaint)
        fs_grievance = FileSystemStorage(location='infra_files/grievance_list')
        path_grievance=str(item.list_of_members_in_grievance_redressal_committee)
        fs_grievance.delete(path_grievance)
        fs_disciplane = FileSystemStorage(location='infra_files/disciplane_list')
        path_disciplane=str(item.list_of_members_in_disciplane_committee)
        fs_disciplane.delete(path_disciplane)
        fs_ST_SC = FileSystemStorage(location='infra_files/ST_SC_list')
        path_ST_SC=str(item.list_of_members_in_ST_SC_cell)
        fs_ST_SC.delete(path_ST_SC)
        fs_disaster= FileSystemStorage(location='infra_files/disaster_mng_list')
        path_disaster=str(item.list_of_members_in_disaster_management_cell)
        fs_disaster.delete(path_disaster)
        fs_NSS= FileSystemStorage(location='infra_files/NSS_list')
        path_NSS=str(item.list_of_members_in_NSS)
        fs_NSS.delete(path_NSS)
        fs_MOU= FileSystemStorage(location='infra_files/Mou_proof')
        tieup_university_details=json.loads(item.tieup_university_details)
        for key in tieup_university_details:
            path_MOU=str(tieup_university_details[key]['tieup_MoU_proof'])
            if(path_MOU != ''):
                fs_MOU.delete(path_MOU)
        Infrastructure.objects.filter(id=id).delete()
        return display_infracolumns(request,'Entry Deleted')
    else:
        return HttpResponse(True)


def edit_infra_entry(request):
    id = request.POST['id_details']
    columns = request.POST['columns_details']
    showFilters = request.POST['show_filters']
    item = Infrastructure.objects.get(pk = id)
    item.date_of_first_AICTE_accreditation=str(item.date_of_first_AICTE_accreditation)
    item.date_of_last_submitted_AQAR_report=str(item.date_of_last_submitted_AQAR_report)
    form = InfraForm(instance=item)
    context = {
        'form':form,
        'columns':columns,
        'id':id,
        'item':item,
        'showFilters':showFilters,
    }
    return render(request,'infrastructure/editInfra.html',context)

def save_infra_entry(request,pk):
    item = Infrastructure.objects.get(id =pk)
    if request.method == "POST":
        item.for_year_infra_entry = request.POST['for_year_infra_entry']
        item.name_of_the_institute = request.POST['name_of_the_institute']
        item.institute_category = request.POST['institute_category']
        item.name_of_affiliating_university = request.POST['name_of_affiliating_university']
        item.institution_status=request.POST['institution_status']
        item.institute_type = request.POST['institute_type']
        item.year_of_establishment = request.POST['yr_of_establishment']
        item.year_of_1st_passout_batch = request.POST['yr_of_1st_passout_batch']
        item.address = request.POST['address']
        item.city=request.POST['city']
        item.state=request.POST['state']
        item.pincode=request.POST['pincode']
        item.campus_area = request.POST['campus_area']
        item.total_built_up_area_in_sqmtr = request.POST['total_built_up_area_in_sqmtr']
        item.total_built_up_area_in_sqft=request.POST['total_built_up_area_in_sqft']
        item.total_playground_area=request.POST['total_playground_area']
        item.phone = request.POST['phone']
        item.email = request.POST['email']
        item.website = request.POST['website']
        item.head_of_the_institute = request.POST['head_of_the_institute']
        item.name_of_the_head_of_institution = request.POST['name_of_the_head_of_institution']
        item.available_courses = request.POST['available_courses']
        item.no_of_voluntary_programs_supported=request.POST['no_of_voluntary_programs_supported']
        item.AICTE_approved = request.POST['AICTE_approved']
        item.date_of_first_AICTE_accreditation = request.POST['date_of_first_AICTE_accreditation']
        item.AICTE_valid_upto = request.POST['AICTE_valid_upto_yr']
        item.NAAC_accredited = request.POST['NAAC_accredited']
        item.year_of_first_NAAC_accreditation = request.POST['yr_of_first_NAAC_accreditation']
        item.latest_NAAC_grade=request.POST['latest_NAAC_grade']
        item.latest_NAAC_score=request.POST['latest_NAAC_score']
        item.NAAC_accreditation_valid_upto=request.POST['NAAC_accreditation_valid_upto_yr']
        item.date_of_last_submitted_AQAR_report=request.POST['date_of_last_submitted_AQAR_report']
        item.ABET_accredited=request.POST['ABET_accredited']
        item.NBA_accredited_courses=request.POST['NBA_accredited_courses']
        item.NBA_accreditation_valid_upto=request.POST['NBA_accreditation_valid_upto_yr']
        item.number_of_classrooms=request.POST['number_of_classrooms']
        item.no_of_seminar_halls=request.POST['no_of_seminar_halls']
        item.no_of_classrooms_with_audio_visual_facility=request.POST['no_of_classrooms_with_audio_visual_facility']
        item.no_of_labs=request.POST['no_of_labs']
        item.no_of_computer_labs=request.POST['no_of_computer_labs']
        item.no_of_auditoriums=request.POST['no_of_auditoriums']
        item.total_sitting_capacity_in_main_auditorium=request.POST['total_sitting_capacity_in_main_auditorium']
        item.no_of_conference_rooms=request.POST['no_of_conference_rooms']
        item.no_of_recreation_rooms=request.POST['no_of_recreation_rooms']
        item.no_of_faculty_cabins=request.POST['no_of_faculty_cabins']
        item.no_of_PCs_provided_to_student=request.POST['no_of_PCs_provided_to_student']
        item.no_of_PCs_provided_to_faculty=request.POST['no_of_PCs_provided_to_faculty']
        item.no_of_PCs_provided_to_other_than_faculty=request.POST['no_of_PCs_provided_to_other_than_faculty']
        item.total_PCs_in_campus=request.POST['total_PCs_in_campus']
        item.no_of_latest_instruments_in_labs=request.POST['no_of_latest_instruments_in_labs']
        item.availability_of_water_recyling_unit=request.POST['availability_of_water_recyling_unit']
        item.availability_of_anti_ragging_cell=request.POST['availability_of_anti_ragging_cell']
        item.availability_of_grievance_redressal_mechanism=request.POST['availability_of_grievance_redressal_mechanism']
        item.availability_of_internal_complaints_commitee=request.POST['availability_of_internal_complaints_commitee']
        item.availability_of_NSS_cell=request.POST['availability_of_NSS_cell']
        item.availability_of_IQAC=request.POST['availability_of_IQAC']
        item.availability_of_faculty_feedback_mechanism=request.POST['availability_of_faculty_feedback_mechanism']
        item.availability_of_alumini_association=request.POST['availability_of_alumini_association']
        item.no_of_alumini=request.POST['no_of_alumini']
        item.availability_of_incubation_centre=request.POST['availability_of_incubation_centre']
        item.no_of_companies_setup_in_last_5_years_by_incubation_centre=request.POST['no_of_companies_setup_in_last_5_years_by_incubation_centre']
        item.hostel_facilities_for_boys=request.POST['hostel_facilities_for_boys']
        item.area_of_boys_hostel=request.POST['area_of_boys_hostel']
        item.capacity_of_boys_hostel=request.POST['capacity_of_boys_hostel']
        item.no_of_boys_in_hostel=request.POST['no_of_boys_in_hostel']
        item.hostel_facilities_for_girls=request.POST['hostel_facilities_for_girls']
        item.area_of_girls_hostel=request.POST['area_of_girls_hostel']
        item.capacity_of_girls_hostel=request.POST['capacity_of_girls_hostel']
        item.no_of_girls_in_hostel=request.POST['no_of_girls_in_hostel']
        item.no_of_students_availing_hostel_facilities=request.POST['no_of_students_availing_hostel_facilities']
        item.residence_facility_for_faculty=request.POST['residence_facility_for_faculty']
        item.total_staff_quarters=request.POST['total_staff_quarters']
        item.how_many_faculties_residing_in_college_campus=request.POST['how_many_faculties_residing_in_college_campus']
        item.no_of_faculties_visited_any_foreign_university_in_previous_AY=request.POST['no_of_faculties_visited_any_foreign_university_in_previous_AY']
        item.institute_tieup_with_foreign_university=request.POST['institute_tieup_with_foreign_university']
        if(request.POST['no_of_tie_up']!=''):
            item.no_of_tie_up=request.POST['no_of_tie_up']
        item.club_details=request.POST['club_details']
        item.no_of_clubs_in_college=request.POST['no_of_clubs_in_college']
        item.canteen=request.POST['canteen']
        item.cricket_ground=request.POST['cricket_ground']
        item.basketball_court=request.POST['basketball_court']
        item.football_ground=request.POST['football_ground']
        item.swimming_pool=request.POST['swimming_pool']
        item.lawn_tennis_court=request.POST['lawn_tennis_court']
        item.badminton_court=request.POST['badminton_court']
        item.bank_branch=request.POST['bank_branch']
        item.wifi_facilities=request.POST['wifi_facilities']
        item.table_tennis_boards=request.POST['table_tennis_boards']
        item.gymnasium=request.POST['gymnasium']
        item.bank_ATM=request.POST['bank_ATM']
        item.no_of_publications_by_college=request.POST['no_of_publications_by_college']
        item.publication_details=request.POST['publication_details']
        now=datetime.now()

        if(request.POST['tieup_university_details']!=''):
            tieup_university_details=json.loads(request.POST['tieup_university_details'])
            old_tieup_university_details=json.loads(item.tieup_university_details)
            for key in tieup_university_details:
                if request.method == 'POST' and "tieup_MoU_proof_"+key in request.FILES and request.FILES['tieup_MoU_proof_'+key]:
                    tieup_MoU_proof =request.FILES['tieup_MoU_proof_'+key]
                    fs = FileSystemStorage(location='infra_files/Mou_proof/')
                    filename = fs.save(now.strftime("%H%M%S")+'_'+key+".pdf", tieup_MoU_proof)
                    uploaded_file_url = fs.url(filename) 
                    fs.delete(old_tieup_university_details[key]['tieup_MoU_proof'])
                    tieup_university_details[key]['tieup_MoU_proof'] = uploaded_file_url.split('/')[-1]
            item.tieup_university_details=json.dumps(tieup_university_details)

        if request.method == 'POST' and "proof_UGC_recognition" in request.FILES and request.FILES['proof_UGC_recognition']:
            proof_UGC_recognition = request.FILES['proof_UGC_recognition']
            fs = FileSystemStorage(location='infra_files/UGC_proof/')
            filename = fs.save(now.strftime("%H%M%S")+".pdf", proof_UGC_recognition)
            uploaded_file_url = fs.url(filename)
            fs.delete(item.proof_UGC_recognition)
            item.proof_UGC_recognition = uploaded_file_url.split('/')[-1]

        if request.method == 'POST' and "proof_yr_of_estb_of_college" in request.FILES and request.FILES['proof_yr_of_estb_of_college']:
            proof_yr_of_estb_of_college = request.FILES['proof_yr_of_estb_of_college']
            fs = FileSystemStorage(location='infra_files/college_estb_proof/')
            filename = fs.save(now.strftime("%H%M%S")+".pdf", proof_yr_of_estb_of_college)
            uploaded_file_url = fs.url(filename)
            fs.delete(item.proof_yr_of_estb_of_college)
            item.proof_yr_of_estb_of_college = uploaded_file_url.split('/')[-1]    

        if request.method == 'POST' and "latest_AICTE_renewed_approval_certificate" in request.FILES and request.FILES['latest_AICTE_renewed_approval_certificate']:
            latest_AICTE_renewed_approval_certificate = request.FILES['latest_AICTE_renewed_approval_certificate']
            fs = FileSystemStorage(location='infra_files/AICTE_renew_proof/')
            filename = fs.save(now.strftime("%H%M%S")+".pdf", latest_AICTE_renewed_approval_certificate)
            uploaded_file_url = fs.url(filename)
            fs.delete(item.latest_AICTE_renewed_approval_certificate)
            item.latest_AICTE_renewed_approval_certificate = uploaded_file_url.split('/')[-1]

        if request.method == 'POST' and "NBA_accreditation_certificate" in request.FILES and request.FILES['NBA_accreditation_certificate']:
            NBA_accreditation_certificate = request.FILES['NBA_accreditation_certificate']
            fs = FileSystemStorage(location='infra_files/NBA_accr_proof/')
            filename = fs.save(now.strftime("%H%M%S")+".pdf", NBA_accreditation_certificate)
            uploaded_file_url = fs.url(filename)
            fs.delete(item.NBA_accreditation_certificate)
            item.NBA_accreditation_certificate = uploaded_file_url.split('/')[-1] 

        if request.method == 'POST' and "NAAC_accreditation_certificate" in request.FILES and request.FILES['NAAC_accreditation_certificate']:
            NAAC_accreditation_certificate = request.FILES['NAAC_accreditation_certificate']
            fs = FileSystemStorage(location='infra_files/NAAC_accr_proof/')
            filename = fs.save(now.strftime("%H%M%S")+".pdf", NAAC_accreditation_certificate)
            uploaded_file_url = fs.url(filename)
            fs.delete(item.NAAC_accreditation_certificate)
            item.NAAC_accreditation_certificate = uploaded_file_url.split('/')[-1]  

        if request.method == 'POST' and "latest_AQAR_submitted_to_NAAC" in request.FILES and request.FILES['latest_AQAR_submitted_to_NAAC']:
            latest_AQAR_submitted_to_NAAC = request.FILES['latest_AQAR_submitted_to_NAAC']
            fs = FileSystemStorage(location='infra_files/AQAR_proof/')
            filename = fs.save(now.strftime("%H%M%S")+".pdf", latest_AQAR_submitted_to_NAAC)
            uploaded_file_url = fs.url(filename)
            fs.delete(item.latest_AQAR_submitted_to_NAAC)
            item.latest_AQAR_submitted_to_NAAC = uploaded_file_url.split('/')[-1] 

        if request.method == 'POST' and "list_of_governing_body_members" in request.FILES and request.FILES['list_of_governing_body_members']:
            list_of_governing_body_members = request.FILES['list_of_governing_body_members']
            fs = FileSystemStorage(location='infra_files/governing_list/')
            filename = fs.save(now.strftime("%H%M%S")+".pdf", list_of_governing_body_members)
            uploaded_file_url = fs.url(filename)
            fs.delete(item.list_of_governing_body_members)
            item.list_of_governing_body_members = uploaded_file_url.split('/')[-1]

        if request.method == 'POST' and "list_of_academic_advisory_body" in request.FILES and request.FILES['list_of_academic_advisory_body']:
            list_of_academic_advisory_body = request.FILES['list_of_academic_advisory_body']
            fs = FileSystemStorage(location='infra_files/academic_list/')
            filename = fs.save(now.strftime("%H%M%S")+".pdf", list_of_academic_advisory_body)
            uploaded_file_url = fs.url(filename)
            fs.delete(item.list_of_academic_advisory_body)
            item.list_of_academic_advisory_body = uploaded_file_url.split('/')[-1]  

        if request.method == 'POST' and "list_of_members_in_anti_ragging_committee" in request.FILES and request.FILES['list_of_members_in_anti_ragging_committee']:
            list_of_members_in_anti_ragging_committee = request.FILES['list_of_members_in_anti_ragging_committee']
            fs = FileSystemStorage(location='infra_files/anti_rag_list/')
            filename = fs.save(now.strftime("%H%M%S")+".pdf", list_of_members_in_anti_ragging_committee)
            uploaded_file_url = fs.url(filename)
            fs.delete(item.list_of_members_in_anti_ragging_committee)
            item.list_of_members_in_anti_ragging_committee = uploaded_file_url.split('/')[-1]                  

        if request.method == 'POST' and "list_of_members_in_internal_complaint_committee" in request.FILES and request.FILES['list_of_members_in_internal_complaint_committee']:
            list_of_members_in_internal_complaint_committee = request.FILES['list_of_members_in_internal_complaint_committee']
            fs = FileSystemStorage(location='infra_files/int_complain_list/')
            filename = fs.save(now.strftime("%H%M%S")+".pdf", list_of_members_in_internal_complaint_committee)
            uploaded_file_url = fs.url(filename)
            fs.delete(item.list_of_members_in_internal_complaint_committee)
            item.list_of_members_in_internal_complaint_committee = uploaded_file_url.split('/')[-1] 

        if request.method == 'POST' and "list_of_members_in_grievance_redressal_committee" in request.FILES and request.FILES['list_of_members_in_grievance_redressal_committee']:
            list_of_members_in_grievance_redressal_committee = request.FILES['list_of_members_in_grievance_redressal_committee']
            fs = FileSystemStorage(location='infra_files/grievance_list/')
            filename = fs.save(now.strftime("%H%M%S")+".pdf", list_of_members_in_grievance_redressal_committee)
            uploaded_file_url = fs.url(filename)
            fs.delete(item.list_of_members_in_grievance_redressal_committee)
            item.list_of_members_in_grievance_redressal_committee = uploaded_file_url.split('/')[-1]       

        if request.method == 'POST' and "list_of_members_in_disciplane_committee" in request.FILES and request.FILES['list_of_members_in_disciplane_committee']:
            list_of_members_in_disciplane_committee = request.FILES['list_of_members_in_disciplane_committee']
            fs = FileSystemStorage(location='infra_files/disciplane_list/')
            filename = fs.save(now.strftime("%H%M%S")+".pdf", list_of_members_in_disciplane_committee)
            uploaded_file_url = fs.url(filename)
            fs.delete(item.list_of_members_in_disciplane_committee)
            item.list_of_members_in_disciplane_committee = uploaded_file_url.split('/')[-1]   

        if request.method == 'POST' and "list_of_members_in_ST_SC_cell" in request.FILES and request.FILES['list_of_members_in_ST_SC_cell']:
            list_of_members_in_ST_SC_cell = request.FILES['list_of_members_in_ST_SC_cell']
            fs = FileSystemStorage(location='infra_files/ST_SC_list/')
            filename = fs.save(now.strftime("%H%M%S")+".pdf", list_of_members_in_ST_SC_cell)
            uploaded_file_url = fs.url(filename)
            fs.delete(item.list_of_members_in_ST_SC_cell)
            item.list_of_members_in_ST_SC_cell = uploaded_file_url.split('/')[-1] 

        if request.method == 'POST' and "list_of_members_in_disaster_management_cell" in request.FILES and request.FILES['list_of_members_in_disaster_management_cell']:
            list_of_members_in_disaster_management_cell = request.FILES['list_of_members_in_disaster_management_cell']
            fs = FileSystemStorage(location='infra_files/disaster_mng_list/')
            filename = fs.save(now.strftime("%H%M%S")+".pdf", list_of_members_in_disaster_management_cell)
            uploaded_file_url = fs.url(filename)
            fs.delete(item.list_of_members_in_disaster_management_cell)
            item.list_of_members_in_disaster_management_cell = uploaded_file_url.split('/')[-1] 

        if request.method == 'POST' and "list_of_members_in_NSS" in request.FILES and request.FILES['list_of_members_in_NSS']:
            list_of_members_in_NSS = request.FILES['list_of_members_in_NSS']
            fs = FileSystemStorage(location='infra_files/NSS_list/')
            filename = fs.save(now.strftime("%H%M%S")+".pdf", list_of_members_in_NSS)
            uploaded_file_url = fs.url(filename)
            fs.delete(item.list_of_members_in_NSS)
            item.list_of_members_in_NSS = uploaded_file_url.split('/')[-1]
        

    item.save()
    return display_infracolumns(request,'Details Edited')

def open_file_UGC_proof(request,file):
    return FileResponse(open('infra_files/UGC_proof/'+file,'rb'), filename=file)  

def open_file_college_estb_proof(request,file):
    return FileResponse(open('infra_files/college_estb_proof/'+file,'rb'), filename=file) 

def open_file_AICTE_renew_proof(request,file):
    return FileResponse(open('infra_files/AICTE_renew_proof/'+file,'rb'), filename=file) 

def open_file_NBA_accr_proof(request,file):
    return FileResponse(open('infra_files/NBA_accr_proof/'+file,'rb'), filename=file)

def open_file_NAAC_accr_proof(request,file):
    return FileResponse(open('infra_files/NAAC_accr_proof/'+file,'rb'), filename=file)

def open_file_AQAR_proof(request,file):
    return FileResponse(open('infra_files/AQAR_proof/'+file,'rb'), filename=file)   

def open_file_governing_list(request,file):
    return FileResponse(open('infra_files/governing_list/'+file,'rb'), filename=file)

def open_file_academic_list(request,file):
    return FileResponse(open('infra_files/academic_list/'+file,'rb'), filename=file)

def open_file_anti_rag_list(request,file):
    return FileResponse(open('infra_files/anti_rag_list/'+file,'rb'), filename=file) 

def open_file_int_complain_list(request,file):
    return FileResponse(open('infra_files/int_complain_list/'+file,'rb'), filename=file)

def open_file_grievance_list(request,file):
    return FileResponse(open('infra_files/grievance_list/'+file,'rb'), filename=file)

def open_file_disciplane_list(request,file):
    return FileResponse(open('infra_files/disciplane_list/'+file,'rb'), filename=file)

def open_file_ST_SC_list(request,file):
    return FileResponse(open('infra_files/ST_SC_list/'+file,'rb'), filename=file)  

def open_file_diasater_mng_list(request,file):
    return FileResponse(open('infra_files/disaster_mng_list/'+file,'rb'), filename=file)     

def open_file_NSS_list(request,file):
    return FileResponse(open('infra_files/NSS_list/'+file,'rb'), filename=file)  

def open_file_mou_proof(request,file):
    return FileResponse(open('infra_files/Mou_proof/'+file,'rb'),filename=file)                            


def export_data(request):
    filter_data = request.POST['filter_data']
    req_col = []
    
    
    if 'columns_details' in request.POST:
            req_col = request.POST['columns_details'].split(',')
            if "id" in req_col:
                req_col.remove('id')
    query = Q()
    if filter_data != "All":
        filter_data = json.loads(filter_data)
        for_year_infra_entry=filter_data['For Year']
        if(for_year_infra_entry != "-1"):
            query = query & Q(for_year_infra_entry = for_year_infra_entry)
        
    
    
    infra_data = Infrastructure.objects.filter(query).values(*req_col)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=infrastructure.csv'
    writer = csv.writer(response)
    req_col.insert(0,'S.no')
    writer.writerow(req_col)
    writer.writerow([])
    i = 1
    for info in infra_data:
        event_row = [i]
        for value in info:
            event_row.append(info[value])
        writer.writerow(event_row)
        i+=1

    return response        