from rest_framework import serializers
from .models import FaultReport

class FaultReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaultReport
        fields = [
            "id", "reporter", "equipment", "assigned_to",
            "description", "priority", "status", "created_at", "updated_at"
        ]
        read_only_fields = ["reporter", "created_at", "updated_at"]