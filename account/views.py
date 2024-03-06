from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, update_session_auth_hash, logout
from django.core.mail import send_mail
from django.conf import settings
from .models import Custom_User
from django.contrib import messages
import random

def signup(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'account/registration.html', {'form': form})

def login(request):
    form = UserLoginForm()
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    return render(request, 'account/login.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('login')






