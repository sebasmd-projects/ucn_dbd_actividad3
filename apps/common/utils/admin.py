from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from .models import RequestLogModel


@admin.register(RequestLogModel)
class RequestLogModelAdmin(ImportExportActionModelAdmin):
    search_fields = (
        'id',
    )
