from django.urls import path, include, re_path
from .views.eventViews import *
from .views.commonViews import *
from .views.studentViews import *
from .views.placementViews import *


urlpatterns = [
    # Report URLs
    path('display_report',display_report,name='display_report'),

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

    # Students url begin
    path('display_students',display_students,name = 'display_students'),
    path('display_students_table',display_students_table,name = 'display_students_table'),
    path('add_student',add_student,name = 'add_student'),
    path('delete_student_entry',delete_student_entry,name = 'delete_student_entry'),
    path('edit_student_entry',edit_student_entry,name = 'edit_student_entry'),
    path('save_student_entry/<int:pk>',save_student_entry,name = 'save_student_entry'),
    path('open_file_proof/<str:file>',open_file_proof,name='open_file_proof'),
    path('filter_student',filter_student,name = 'filter_student'),

    # Placements URLs
    path('placements/',placements,name="placements"),
    path('placements/add_placement_details/',add_placement_details,name="placements/add_placement_details/"),
    path('placements/display_columns/',display_placement_columns,name="placements/display_columns/"),
    path('placement/add_student_placement_detail/',add_student_placement_detail,name="placement/add_student_placement_detail/"),
    path('placement/edit_placement_detail/',edit_placement_detail,name="placement/edit_placement_detail/"),
    path('placement/delete_placement_entry/',delete_placement_entry,name="placement/delete_placement_entry/"),
    
]
