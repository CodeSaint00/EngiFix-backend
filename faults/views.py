from django.utils import timezone
from rest_framework import viewsets, permissions
from .models import FaultReport
from .serializers import FaultReportSerializer

class FaultReportViewSet(viewsets.ModelViewSet):
    queryset = FaultReport.objects.all()
    serializer_class = FaultReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(reporter=self.request.user)

    def perform_update(self, serializer):
        instance = serializer.instance
        new_status = serializer.validated_data.get("status")
        if new_status == "RESOLVED" and instance.status != "RESOLVED":
            serializer.save(resolved_at=timezone.now())
        else:
            serializer.save()