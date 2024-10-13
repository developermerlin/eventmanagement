# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User  # Import the User model
from .forms import CustomRegistrationForm  # Import your custom form
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm

def register(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            # Create a new user instance
            user = User(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['firstname'],
                last_name=form.cleaned_data['lastname'],
                email=form.cleaned_data.get('email'),  # Assuming you want to add an email field in the form
            )
            user.set_password(form.cleaned_data['password'])  # Set the password properly
            user.save()  
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('login')  # Redirect to the login page after success
    else:
        form = CustomRegistrationForm()  # Create a new form instance for GET requests

    return render(request, 'accounts/register.html', {'form': form})  # Render the form




def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to a desired page after login
            else:
                # Use Django's messages framework to add an error message
                messages.error(request, "Invalid username or password.")
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')  