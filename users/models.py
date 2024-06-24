from django.db import models
from django.contrib.auth.models import AbstractUser

from django_countries import countries

NATIONALITY_CHOICES = [(code, name) for code, name in list(countries)]

class User(AbstractUser):
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    emergency_contact_number = models.CharField(max_length=20, null=True, blank=True)
    nationality = models.CharField(max_length=2, choices=NATIONALITY_CHOICES, blank=True, null=True)

    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    is_guest = models.BooleanField(default=True)

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.is_superuser
