from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm


def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid:
            try:
                form.save()
            except:
                return render(request, "authentication/register.html", {'form': form})
            messages.info(request, ("Account successfuly created"))	
            return redirect('home')
    else:
        form = RegisterUserForm()
        return render(request, "authentication/register.html", {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, ("Invalid credentials, try again..."))	
            return redirect('login')
    else:
        return render(request, "authentication/login.html", {})

def logout_user(request):
    logout(request)
    messages.warning(request, ("You were successfuly logged out"))	
    return redirect('home')