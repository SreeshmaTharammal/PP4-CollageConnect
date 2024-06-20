# users/forms.py

from django import forms
from allauth.account.forms import SignupForm
from .models import User

class GuestSignupForm(SignupForm):
    address = forms.CharField(max_length=255, required=False)
    phone_number = forms.CharField(max_length=15, required=False)
    emergency_contact_number = forms.CharField(max_length=15, required=False)
    nationality = forms.CharField(max_length=50, required=False)

    def save(self, request):
        user = super(GuestSignupForm, self).save(request)
        user.address = self.cleaned_data['address']
        user.phone_number = self.cleaned_data['phone_number']
        user.emergency_contact_number = self.cleaned_data['emergency_contact_number']
        user.nationality = self.cleaned_data['nationality']
        user.is_guest = True  # Set to guest by default
        user.is_student = False  # Default to non-student
        user.is_approved = False  # Default to not approved
        user.save()
        return user
