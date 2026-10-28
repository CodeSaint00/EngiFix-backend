from rest_framework import serializers
from .models import Equipment

class EquipmentSerializer(serializers.ModelSerializer):
    location_name = serializers.StringRelatedField(source="location", read_only=True)

    class Meta:
        model = Equipment
        fields = [
            "id", "location", "location_name", "name", "category",
            "serial_number", "condition", "installed_date",
        ]