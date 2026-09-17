from rest_framework import viewsets
from .models import FaultReport
from .serializers import FaultReportSerializer

class FaultReportViewSet(viewsets.ModelViewSet):
    queryset = FaultReport.objects.all()
    serializer_class = FaultReportSerializer