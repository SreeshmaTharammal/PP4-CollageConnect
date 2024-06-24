from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    is_guest = models.BooleanField(default=True)
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    emergency_contact_number = models.CharField(max_length=15, blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)


    @property
    def is_admin(self):
        return self.is_superuser
