from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User, auth
from accounts.models import UserInfo
from .forms import NewDriver

# Create your views here.

def register(request):

    if request.method == "POST":

        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username taken')
                print('Username taken')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password1,email=email)
                user.save()
                print('User created')
                return redirect('travel')
        else:
            print('password not matching')
            messages.error(request,'password not matching')
            return redirect('register')
        
    else:
        return render(request,'accounts/register.html')

   

    


def login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('travel')
        else:
            messages.error(request, 'Неверные данные')
            return redirect('login')
        
    else:
        return render(request,'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('travel')

def cabinet(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'UserInfo'):
            pk=User.pk
            Info = get_object_or_404(UserInfo, pk=pk)
            return render(request,'accounts/driver-cabinet.html',{'Info':Info})
        else:
            return render(request, 'accounts/cabinet.html')
    else:
        return redirect('login')

def driver_new(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = NewDriver(request.POST)
            if form.is_valid():
                driver = form.save(commit=False)
                driver.user = User.pk
                driver.save()
                return redirect('cabinet')
        else:
            form = NewDriver()
            return render(request, 'accounts/new_driver', {'form': form})
    else:
        return redirect('login')

