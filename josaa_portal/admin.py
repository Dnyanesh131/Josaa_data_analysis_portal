from django.contrib import admin
from .models import Ques1
from .models import Ques2
from .models import Ques3
from .models import Ques4
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Ques1)
@admin.register(Ques2)
@admin.register(Ques3)
@admin.register(Ques4)
class ViewAdmin(ImportExportModelAdmin):
    pass
