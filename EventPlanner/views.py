from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.db.models import Q
from django.conf import settings

def Home(request):
    return render(request,'MainHome.html')

def Wedding(request):
    return render(request,'Home.html')

def Venues(request):
    return render(request,'Venues.html')

def Cart(request):
    return render(request,'Cart.html')

def Order(request):
    return render(request,'Order.html')

def AboutUs(request):
    return render(request,'AboutUs.html')

def Registration(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        email=request.POST['email']
        password=request.POST['password']

        if User.objects.filter(email=email).exists():
            messages.error(request, "This email is already taken. Please try another email.")
            return redirect('registration')
        else:
            user = User.objects.create_user(first_name=first_name,username=email,email=email,password=password)
            user.save()
            messages.success(request, "You have Successfully Registered.")
            return redirect('login')
    return render(request,'Registration.html')

def Login(request):
    return render(request,'Login.html')

def ForgetPassword(request):
    return render(request,'ForgetPassword.html')