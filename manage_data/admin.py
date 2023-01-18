from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django.apps import apps
# Register your models here.

models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

class ViewAdmin(ImportExportModelAdmin):
    pass