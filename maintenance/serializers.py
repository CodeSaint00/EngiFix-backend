from rest_framework import serializers
from .models import MaintenanceRecord

class MaintenanceRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaintenanceRecord
        fields = ["id", "fault", "technician", "diagnosis", "action_taken", "started_at", "completed_at"]
        read_only_fields = ["started_at"]