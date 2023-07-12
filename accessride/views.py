from django.shortcuts import render,redirect
from .models import detail,driverdetail
from django.contrib.auth.models import User, auth 
from django.contrib import messages

def home(request):
    details=detail.objects.count()
    feedback_count=detail.objects.exclude(passenger_feedback='').count()
    driverdetails=driverdetail.objects.count()
    return render(request, 'home.html',{'details':details,'driverdetails':driverdetails,'feedback_count':feedback_count})

def adminpanel(request):
    details=detail.objects.all()
    driverdetails=driverdetail.objects.all()
    return render(request,'adminpanel.html',{'details':details,'driverdetails':driverdetails})

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        
        if password1==password2:
            if User.objects.filter(username=username).exists():
               messages.info(request,'Username taken')
               return redirect('accessride:register')
            elif User.objects.filter(email=email).exists():
               messages.info(request,'email taken')
               return redirect('accessride:register')
            else:
              user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
              user.save()
              print('user created')
              return redirect('accessride:login')
        else:
           messages.info(request,'Password not matching')
           return redirect('accessride:register')
        
    else:
         return render(request,'register.html')
    
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        submit=request.POST['submit_button']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            if submit=='driver':
                return redirect('accessride:drivers')
            else:
                return redirect('accessride:passenger')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('accessride:login')
    else:
        return render(request,'login.html')

def drivers(request):
    return render(request,'drivers.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def passenger(request):
    return render(request,'passengers.html')
