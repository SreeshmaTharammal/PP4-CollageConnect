from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm, UserProfileForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required

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


def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin_dashboard')
            else:
                return redirect('user_dashboard')
        else:
            # Handle invalid login credentials
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})

    return render(request, 'login.html')

@login_required
def user_dashboard(request):
    context = {
        'title': 'User Dashboard',
        'message': 'Welcome to your Dashboard!'
    }
    return render(request, 'user_dashboard.html', context)

@login_required
def admin_dashboard(request):
    context = {
        'title': 'Admin Dashboard',
        'message': 'Welcome to the Admin Dashboard!'
    }
    return render(request, 'admin_dashboard.html', context)


