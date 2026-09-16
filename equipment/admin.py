from django.contrib import admin
from .models import Equipment

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ("name", "serial_number", "category", "condition", "location")
    list_filter = ("condition", "category")
    search_fields = ("name", "serial_number")