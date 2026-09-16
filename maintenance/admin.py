from django.contrib import admin
from .models import MaintenanceRecord

@admin.register(MaintenanceRecord)
class MaintenanceRecordAdmin(admin.ModelAdmin):
    list_display = ("id", "fault", "technician", "started_at", "completed_at")
    list_filter = ("technician",)
    search_fields = ("diagnosis", "action_taken")