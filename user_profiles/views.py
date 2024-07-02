from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm, UserProfileForm
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

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
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'user_profile/login.html', {'error': 'Invalid username or password'})
    return render(request, 'user_profile/login.html')

def custom_logout(request):
    logout(request)
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'A user with that username already exists.')
            else:
                user = User.objects.create_user(username=username, password=password)
                UserProfile.objects.create(
                    user=user,
                    address=form.cleaned_data['address'],
                    phone_number=form.cleaned_data['phone_number'],
                    emergency_contact_number=form.cleaned_data['emergency_contact_number'],
                    nationality=form.cleaned_data['nationality'],
                    is_guest=True
                )
                login(request, user)
                return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'user_profile/signup.html', {'form': form})

@login_required
def dashboard(request):
    print("Debug: dashboard")
    try:
        user_profile = request.user.userprofile
    except ObjectDoesNotExist:
        return redirect('create_user_profile')
    if request.user.is_superuser:
        return redirect('admin_dashboard')
    elif user_profile.is_student:
        return redirect('student_dashboard')
    elif user_profile.is_instructor:
        return redirect('instructor_dashboard')
    elif user_profile.is_guest:
        return redirect('guest_dashboard')
    else:
        return redirect('home')

@login_required
def admin_dashboard(request):
    user_profile = request.user.userprofile
    if not user_profile.is_admin:
        return redirect('dashboard')  # Redirect non-admins to their appropriate dashboard

    enrollments = Enrollment.objects.filter(is_approved=False)
    if request.method == 'POST':
        enrollment_id = request.POST.get('enrollment_id')
        enrollment = Enrollment.objects.get(id=enrollment_id)
        enrollment.is_approved = True
        enrollment.save()
        user_profile = enrollment.user_profile
        user_profile.is_guest = False
        user_profile.is_student = True
        user_profile.save()
        return redirect('admin_dashboard')

    return render(request, 'courses/admin_dashboard.html', {'enrollments': enrollments})

@login_required
def student_dashboard(request):
    return render(request, 'user_profile/student_dashboard.html')

@login_required
def instructor_dashboard(request):
    return render(request, 'user_profile/instructor_dashboard.html')