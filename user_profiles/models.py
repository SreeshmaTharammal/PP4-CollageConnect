# user_profiles/models.py
from django.db import models
from django.contrib.auth.models import User
from .choices import NATIONALITY_CHOICES
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    nationality = models.CharField(max_length=2, choices=NATIONALITY_CHOICES)
    phone_number = models.CharField(max_length=15)
    emergency_contact_number = models.CharField(max_length=15)
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_guest = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

