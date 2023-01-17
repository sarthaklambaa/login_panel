from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username').lower()
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if not first_name or not last_name:
            return HttpResponse("First name and Last name is required.")

        if pass1 != pass2:
            return redirect("password_error")

        existing_user = User.objects.filter(username=username).exists()
        if existing_user:
            return redirect('username_taken')

        user = User.objects.create_user(username,email=email)
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(pass1)
        user.save()
        return redirect('successful')

    return render(request, 'signup.html')


def login_page (request):
    if request.method == 'POST':
        username=request.POST.get('username').lower()
        pass1=request.POST.get('pass')
        user=authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request,user)
            return redirect ('home')

        else:
            return redirect('fail')

    return render(request, 'login.html')

def user_created (request):
    return render(request,'user_created.html')
    
def username_taken (request):
    return render(request,'username_taken.html')
    
def password_error (request):
    return render(request,'password_error.html')

def fail (request):
    return render(request,'fail.html')

def logout_page(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home_page (request):
    return render(request, 'home.html')

