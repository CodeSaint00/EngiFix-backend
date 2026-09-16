from django.db import models
from locations.models import Location

class Equipment(models.Model):
    class Condition(models.TextChoices):
        OPERATIONAL = "OPERATIONAL", "Operational"
        UNDER_MAINTENANCE = "UNDER_MAINTENANCE", "Under Maintenance"
        FAULTY = "FAULTY", "Faulty"
        DECOMMISSIONED = "DECOMMISSIONED", "Decommissioned"

    location = models.ForeignKey(Location, on_delete=models.PROTECT, related_name="equipment")
    name = models.CharField(max_length=150)
    category = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    condition = models.CharField(max_length=30, choices=Condition.choices, default=Condition.OPERATIONAL)
    installed_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.serial_number})"