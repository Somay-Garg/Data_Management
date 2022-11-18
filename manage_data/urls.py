from django.urls import path
from .views import *

urlpatterns = [

    path('',display_events,name='display_events'),

    path('display_events',display_events,name='display_events'),
    path('add_event',add_event,name='add_event'),
    path('edit_event/<int:pk>',edit_event,name='edit_event'),
    path('delete_event/<int:pk>',delete_event,name='delete_event'),
    path('filter_events',filter_events,name='filter_events'),
    path('open_file_atten/<str:file>',open_file_atten,name='open_file_atten'),
    path('open_file_report/<str:file>',open_file_report,name='open_file_report'),
]