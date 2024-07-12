from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')
def createseller(request):
    if request.POST:
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        
        if not username or not email or not password or not confirmpassword:
            messages.error(request,'all fields are required.')

        elif confirmpassword != password:
            messages.error(request,"password doesnot match")
           
        elif User.objects.filter(email=email).exists():
            messages.error(request,"email already exist")
           
        elif User.objects.filter(username=username).exists():
            messages.error(request,"username already exist")

        else:
           
            user = User.objects.create_user(username=username, email=email, password=password)    
            user.is_staff=True
            user.save()
            messages.success(request,"account created successfully")
            return render(request, "sellercreate.html")
    return render(request,"sellercreate.html")    


def sellerlogin(request):
    if 'username' in request.session:
        return redirect('sellerindex')
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            request.session['username']=username
            return redirect("sellerindex")
    return render(request,"sellerlogin.html") 

def sellerindex(request):
    return render(request,"sellerindex.html")

def logoutseller(request):
    logout(request)
    request.session.flush()
    return redirect('sellerlogin')
def logoutuser(request):
    logout(request)
    request.session.flush()
    return redirect('index')

def usersignup(request):
    if request.POST:
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirmpassword=request.POST.get('confirmpassword')
        
        if not username or not email or not password or not confirmpassword:
            messages.error(request,'all fields are required.')

        elif confirmpassword != password:
            messages.error(request,"password doesnot match")
           
        elif User.objects.filter(email=email).exists():
            messages.error(request,"email already exist")
           
        elif User.objects.filter(username=username).exists():
            messages.error(request,"username already exist")

        else:
           
            user = User.objects.create_user(username=username, email=email, password=password)    
            user.save()
            messages.success(request,"account created successfully")
            return render(request, "usercreate.html")
    return render(request,"usercreate.html") 


def userlogin(request):
    if 'username' in request.session:
        return redirect('index', user=request.user.username)  
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            request.session['username'] = username
            return redirect('index')  
        
    return render(request, 'userlogin.html') 