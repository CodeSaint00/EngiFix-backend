from rest_framework import viewsets
from .models import MaintenanceRecord
from .serializers import MaintenanceRecordSerializer

class MaintenanceRecordViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceRecord.objects.all()
    serializer_class = MaintenanceRecordSerializer