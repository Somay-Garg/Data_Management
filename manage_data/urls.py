from django.urls import path
from .views.eventViews import *
from .views.commonViews import *
from .views.studentViews import *
from .views.placementViews import *
from .views.infraViews import *

urlpatterns = [
    # Event URLs
    path('',display_events,name='display_events'),
    path('display_events',display_events,name='display_events'),
    path('add_event',add_event,name='add_event'),
    path('edit_event/<int:pk>',edit_event,name='edit_event'),
    path('display_columns',display_columns,name='display_columns'),
    path('open_file_atten/<str:file>',open_file_atten,name='open_file_atten'),
    path('open_file_report/<str:file>',open_file_report,name='open_file_report'),
    path('save_event/<int:pk>',save_event,name = 'save_event'),
    path('edit_event',edit_event,name = 'edit_event'),
    path('filter_event',filter_event,name = 'filter_event'),
    path('delete_event_entry',delete_event_entry,name = 'delete_event_entry'),
    # Report URLs
    path('display_report', display_report,name='display_report'),
    # Students url begin
    path('display_students',display_students,name = 'display_students'),
    path('display_students_table',display_students_table,name = 'display_students_table'),
    path('add_student',add_student,name = 'add_student'),
    path('delete_student_entry',delete_student_entry,name = 'delete_student_entry'),
    path('edit_student_entry',edit_student_entry,name = 'edit_student_entry'),
    path('save_student_entry/<int:pk>',save_student_entry,name = 'save_student_entry'),
    path('open_file_proof/<str:file>',open_file_proof,name='open_file_proof'),
    path('filter_student',filter_student,name = 'filter_student'),
    # students url end

    # Placements URLs
    path('placements/',placements,name="placements"),
    path('placements/add_placement_details/',add_placement_details,name="placements/add_placement_details/"),
    path('placements/display_columns/',display_placement_columns,name="placements/display_columns/"),
    path('placements/add_student_placement_detail/',add_student_placement_detail,name="placements/add_student_placement_detail/"),
    path('placements/edit_placement_detail/',edit_placement_detail,name="placements/edit_placement_detail/"),
    path('placements/delete_placement_entry/',delete_placement_entry,name="placements/delete_placement_entry/"),
    path('placements/filter_placement/',filter_placement,name="placements/filter_placement/"),
    path('placements/save_student_placement_detail/',save_student_placement_detail,name="placements/save_student_placement_detail/"),
    path('placements/show_placement_detail/<int:pk>/<str:showFilters>',show_placement_detail,name="placements/show_placement_detail/"),
    path('placements/open_offer_proof/<str:file>/',open_offer_proof,name="placements/open_offer_proof/"),
    path('placements/open_exam_proof/<str:file>/',open_exam_proof,name="placements/open_exam_proof/"),
    path('placements/open_current_status_proof/<str:file>/',open_current_status_proof,name="placements/open_current_status_proof/"),

    #Infrastructure URLs
    path('display_infra',display_infra,name='display_infra'),
    path('add_infra',add_infra,name='add_infra'),
    path('filter_infra',filter_infra,name = 'filter_infra'),
    path('display_infracolumns',display_infracolumns,name='display_infracolumns'),
    path('delete_infra_entry',delete_infra_entry,name = 'delete_infra_entry'),
    path('edit_infra_entry',edit_infra_entry,name = 'edit_infra_entry'),
    path('save_infra_entry/<int:pk>',save_infra_entry,name = 'save_infra_entry'),
    path('open_file_UGC_proof/<str:file>',open_file_UGC_proof,name='open_file_UGC_proof'),
    path('open_file_college_estb_proof/<str:file>',open_file_college_estb_proof,name='open_file_college_estb_proof'),
    path('open_file_AICTE_renew_proof/<str:file>',open_file_AICTE_renew_proof,name='open_file_AICTE_renew_proof'),
    path('open_file_NBA_accr_proof/<str:file>',open_file_NBA_accr_proof,name='open_file_NBA_accr_proof'),
    path('open_file_NAAC_accr_proof/<str:file>',open_file_NAAC_accr_proof,name='open_file_NAAC_accr_proof'),
    path('open_file_AQAR_proof/<str:file>',open_file_AQAR_proof,name='open_file_AQAR_proof'),
    path('open_file_governing_list/<str:file>',open_file_governing_list,name='open_file_governing_list'),
    path('open_file_academic_list/<str:file>',open_file_academic_list,name='open_file_academic_list'),
    path('open_file_anti_rag_list/<str:file>',open_file_anti_rag_list,name='open_file_anti_rag_list'),
    path('open_file_int_complain_list/<str:file>',open_file_int_complain_list,name='open_file_int_complain_list'),
    path('open_file_grievance_list/<str:file>',open_file_grievance_list,name='open_file_grievance_list'),
    path('open_file_disciplane_list/<str:file>',open_file_disciplane_list,name='open_file_disciplane_list'),
    path('open_file_ST_SC_list/<str:file>',open_file_ST_SC_list,name='open_file_ST_SC_list'),
    path('open_file_diasater_mng_list/<str:file>',open_file_diasater_mng_list,name='open_file_diasater_mng_list'),
    path('open_file_NSS_list/<str:file>',open_file_NSS_list,name='open_file_NSS_list'),
    path('open_file_mou_proof/<str:file>',open_file_mou_proof,name='open_file_mou_proof'),
]
