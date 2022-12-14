from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.backends import ModelBackend
# Create your views here.

def homePage(request):
    curentUser = request.user
    if request.POST.get('logout'):
        logoutUser(request)
    if (request.user.is_anonymous == False):
        return render(request,'home.html',{ 'current' : curentUser })
    else :
        return render(request,'home.html',{ 'current' : False })
        

@login_required
def logoutUser(request):
    logout(request)

    return redirect('home')
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        print(email,password)
        try:
            user = authenticate(request,username=email,password=password)
            print(user)
        except Exception as e:
            user=None
        if user is not None:
            login(request,user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
        else:
            messages.success(request,'Login failed')
    return render(request, 'login.html')

def registerPage(request):
    if request.method == 'POST':
        username = request.POST.get('email').lower()
        password = request.POST.get('password1')
        name = request.POST.get('name')
        confirm_password = request.POST.get("password2")
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        if( password != confirm_password):
            messages.success(request,'mật khẩu không trùng!')
            return render(request,'base/register.html')
        try:
            user = User.objects.get(email=email)
        except:
            user=User(name=name,email=username,phone=phone)
            user.password =make_password(password)
            user.save()
            messages.success(request,'Register success!')
            return redirect('login')

        if user is not None:
            messages.success(request,'Account already exists!')
    return render(request,'register.html')