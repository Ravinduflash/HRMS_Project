from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from.forms import SignUpForm, LoginForm
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('dashboard')  # Change this to your dashboard URL
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Change this to your dashboard URL
            else:
                form.add_error(None, "Invalid username or password")
        signup_form = SignUpForm()  # Define signup_form here
    else:
        form = LoginForm()
        signup_form = SignUpForm()  # Define signup_form here
    return render(request, 'registration/login.html', {'form': form, 'signup_form': signup_form})