from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from .choices import NATIONALITY_CHOICES

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserProfileForm(forms.ModelForm):
    nationality = forms.ChoiceField(choices=NATIONALITY_CHOICES)

    class Meta:
        model = UserProfile
        fields = ['address', 'phone_number', 'emergency_contact_number', 'nationality', 'is_student', 'is_instructor', 'is_admin', 'is_guest']

class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)
    address = forms.CharField(max_length=255, required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    emergency_contact_number = forms.CharField(max_length=15, required=True)
    nationality = forms.ChoiceField(choices=NATIONALITY_CHOICES, required=True)

    class Meta:
        model = UserProfile
        fields = ['username', 'password', 'address', 'phone_number', 'emergency_contact_number', 'nationality']

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user_profile = UserProfile.objects.create(
                user=user,
                address=self.cleaned_data['address'],
                phone_number=self.cleaned_data['phone_number'],
                emergency_contact_number=self.cleaned_data['emergency_contact_number'],
                nationality=self.cleaned_data['nationality'],
                is_guest=True
            )
        return user
