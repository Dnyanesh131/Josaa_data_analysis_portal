from django.contrib import admin

from .models import Datareq
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Datareq)
class ViewAdmin(ImportExportModelAdmin):
    pass
