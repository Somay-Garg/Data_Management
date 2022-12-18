# from operator import or_
from django.shortcuts import render, redirect, get_object_or_404
# from django.core.files.storage import FileSystemStorage
# from manage_data.models.eventsModel import *
# from ..forms import *
# from django.db.models import Q
from django.http import HttpResponse
# from django.http import FileResponse
# from datetime import datetime
# import json
# import csv
# from django.views.decorators.csrf import csrf_exempt

def display_report(request):
    return render(request,'report.html')