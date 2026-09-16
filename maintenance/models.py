from django.conf import settings
from django.db import models
from faults.models import FaultReport

class MaintenanceRecord(models.Model):
    fault = models.ForeignKey(
        FaultReport, on_delete=models.CASCADE, related_name="maintenance_records"
    )
    technician = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="maintenance_records"
    )
    diagnosis = models.TextField()
    action_taken = models.TextField()
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Record for {self.fault} by {self.technician}"