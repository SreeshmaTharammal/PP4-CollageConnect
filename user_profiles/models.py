from django.db import models
from django.contrib.auth.models import User

NATIONALITY_CHOICES = [
    ('USA', 'United States of America'),
    ('CAN', 'Canada'),
    ('IE', 'Ireland'),  
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    emergency_contact_number = models.CharField(max_length=15, null=True, blank=True)
    nationality = models.CharField(max_length=3, choices=NATIONALITY_CHOICES, null=True, blank=True)
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_guest = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
