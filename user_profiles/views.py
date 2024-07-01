from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm, UserProfileForm
from .models import UserProfile

def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)  # Hash the password
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('profile')
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'user_profile/register.html', {'user_form': user_form, 'profile_form': profile_form})

def profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'user_profile/profile.html', {'user_profile': user_profile})
