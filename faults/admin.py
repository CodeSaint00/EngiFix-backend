from django.contrib import admin
from .models import FaultReport

@admin.register(FaultReport)
class FaultReportAdmin(admin.ModelAdmin):
    list_display = ("id", "equipment", "reporter", "assigned_to", "status", "priority", "created_at")
    list_filter = ("status", "priority")
    search_fields = ("description", "equipment__name")