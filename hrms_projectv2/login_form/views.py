from django.contrib.auth import login, authenticate
from django.contrib.auth.models import Group
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Login successful.')
                if user.groups.filter(name='HR Managers').exists():
                    return render(request, 'registration/login.html', {'form': form, 'signup_form': SignupForm(), 'redirect_url': 'hr_manager_dashboard'})
                elif user.groups.filter(name='Employees').exists():
                    return render(request, 'registration/login.html', {'form': form, 'signup_form': SignupForm(), 'redirect_url': 'employee_dashboard'})
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = LoginForm()
    signup_form = SignupForm()
    return render(request, 'registration/login.html', {'form': form, 'signup_form': signup_form})

def signup_view(request):
    if request.method == 'POST':
        signup_form = SignupForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save(commit=False)
            user.set_password(signup_form.cleaned_data.get('password1'))
            user.save()
            user_type = signup_form.cleaned_data.get('user_type')
            if user_type == 'HR Manager':
                group = Group.objects.get(name='HR Managers')
            else:
                group = Group.objects.get(name='Employees')
            user.groups.add(group)
            messages.success(request, 'Signup successful. Please log in.')
            return redirect('login')
        else:
            for field, errors in signup_form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    return redirect('login')
