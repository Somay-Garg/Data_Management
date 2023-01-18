from django.urls import path
from .views.eventViews import *
from .views.infraViews import *
from .views.commonViews import *

urlpatterns = [
    # Event URLs
    path('',display_events,name='display_events'),
    path('display_events',display_events,name='display_events'),
    path('add_event',add_event,name='add_event'),
    path('edit_event/<int:pk>',edit_event,name='edit_event'),
    path('display_columns',display_columns,name='display_columns'),
    path('open_file_atten/<str:file>',open_file_atten,name='open_file_atten'),
    path('open_file_report/<str:file>',open_file_report,name='open_file_report'),
    path('display_columns/deleteEvent/',deleteEvent,name = 'deleteEvent'),
    path('deleteEvent',deleteEvent,name = 'deleteEvent'),
    path('save_event/<int:pk>/deleteEvent',deleteEvent,name = 'deleteEvent'),
    path('save_event/deleteEvent',deleteEvent,name = 'deleteEvent'),
    path('save_event/<int:pk>',save_event,name = 'save_event'),
    path('edit_event',edit_event,name = 'edit_event'),
    path('filter_event',filter_event,name = 'filter_event'),

    # Report URLs
    path('display_report',display_report,name='display_report'),

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
