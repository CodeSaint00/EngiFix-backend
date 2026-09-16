from django.db import models
from departments.models import Department

class Location(models.Model):
    department = models.ForeignKey(Department, on_delete=models.PROTECT, related_name="locations")
    building = models.CharField(max_length=100)
    room = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.building} - {self.room}" if self.room else self.building