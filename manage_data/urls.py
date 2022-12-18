from django.urls import path
from .views.eventViews import *
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
]
