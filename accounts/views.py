from django.contrib import messages,auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
# Create your views here.
def Login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request,'Invaild login credentials')
            return redirect('login')
    return render(request,'account/login.html')

def Register(request):
    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email already exists!')
                    return redirect('register')
                else:
                    user=User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                    auth.login(request,user)
                    messages.success(request,'You are now logged in.')
                    return redirect('dashboard')
                    user.save()
                    messages.success(request,'Your are register successfully.')
                    return redirect('login')
        else:
            messages.error(request,'Password do not match')
            return redirect('register')
    else:
        return render(request,'account/register.html')

def Dashboard(request):
    return render(request,'account/dashboard.html')

def Logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are successfully logged out.')
    return redirect('home')