from rest_framework import serializers
from .models import FaultReport

class FaultReportSerializer(serializers.ModelSerializer):
    location_name = serializers.StringRelatedField(source="location", read_only=True)

    class Meta:
        model = FaultReport
        fields = [
            "id", "reporter", "location", "location_name", "equipment", "assigned_to",
            "description", "priority", "status", "image",
            "created_at", "updated_at", "resolved_at"
        ]
        read_only_fields = ["reporter", "created_at", "updated_at", "resolved_at"]
        extra_kwargs = {
            "location": {"required": True, "allow_null": False},
        }