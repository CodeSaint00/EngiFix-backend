import uuid
from django.db import models

class Equipment(models.Model):
    class Condition(models.TextChoices):
        OPERATIONAL = "OPERATIONAL", "Operational"
        UNDER_MAINTENANCE = "UNDER_MAINTENANCE", "Under Maintenance"
        FAULTY = "FAULTY", "Faulty"
        DECOMMISSIONED = "DECOMMISSIONED", "Decommissioned"

    location = models.CharField(max_length=200)
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True, blank=True)
    condition = models.CharField(max_length=30, choices=Condition.choices, default=Condition.OPERATIONAL)
    installed_date = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.serial_number:
            self.serial_number = f"EQ-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.serial_number})"