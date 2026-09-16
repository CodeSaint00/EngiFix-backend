from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        STUDENT = "STUDENT", "Student/Staff"
        TECHNICIAN = "TECHNICIAN", "Technician"
        ADMIN = "ADMIN", "Administrator"
        MANAGEMENT = "MANAGEMENT", "Management/Viewer"

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.STUDENT)