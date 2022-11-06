from django.urls import path
from .views import *

urlpatterns = [
    path('',display_events,name='display_events'),

    path('display_events',display_events,name='display_events'),

    path('add_event',add_event,name='add_event'),

    path('edit_event/<int:pk>',edit_event,name='edit_event'),

    path('delete_event/<int:pk>',delete_event,name='delete_event'),

]