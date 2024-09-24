from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Signup view
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            messages.success(request, 'Account created successfully')
            return redirect('login')
    return render(request, 'accountmanager/signup.html')

# Login view
def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)  # No conflict with renamed view
            messages.success(request, 'Logged in successfully')
            return redirect('profile')  # Make sure 'home' URL exists in urls.py
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'accountmanager/login.html')

# Logout view
def logout_page(request):
    logout(request)  # No conflict with renamed view
    messages.success(request, 'Logged out successfully')
    return redirect('login')

# Profile view
def profile_page(request):
    return render(request, 'accountmanager/profile.html')
