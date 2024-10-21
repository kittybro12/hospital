from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Userdata


def home(request):
    return render(request,'home.html')


def signup_page(request , method=['GET','POST']):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password1 =request.POST.get('password1')
        password2 =request.POST.get('password2')

        user=Userdata.objects.filter(email=email) 

        if user:
            messages.info(request,'User is already exists')
        elif password1 != password2:
            messages.info(request,'Passwords did not match')
        else:
            Userdata.objects.create(email=email,password=password1)       
            return render(request,'login.html') 
    
    return render(request,'signup.html ')
            


def login_page(request,method = ['GET','POST']):
    if request.method == 'POST':
        email = request.POST.get('email')
        password =request.POST.get('password')
        users=Userdata.objects.filter(email=email,password=password)
        
        if users.exists():
            request.session["email"]=email
            return redirect('/main/')
        else:
            messages.info(request,'Email and password is incorrect')
            return render(request,'login.html')        
    
    return render(request,'login.html')




def main(request):
    return render(request,'main.html')


def about(request):
    return render(request,'about.html')

    





