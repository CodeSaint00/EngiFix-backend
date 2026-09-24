from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = "STUDENT", "Student/Staff"
        TECHNICIAN = "TECHNICIAN", "Technician"
        ADMIN = "ADMIN", "Administrator"
        MANAGEMENT = "MANAGEMENT", "Management/Viewer"

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.STUDENT)

    # Student-specific
    department = models.ForeignKey(
        "departments.Department", on_delete=models.SET_NULL, null=True, blank=True
    )
    reg_number = models.CharField(max_length=50, blank=True)

    # Technician-specific
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    is_verified = models.BooleanField(default=True)