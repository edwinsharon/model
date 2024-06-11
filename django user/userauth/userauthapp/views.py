from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import path
# Create your views here.
def userlogin(request):
   
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)  
            request.session['username']=username
            return render(request,"index.html",{"user":user})
        else:
            return redirect ('userlogin')
    if 'username' in request.session:
        return redirect(index)    
    return render(request,"login.html")    

def createuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, password=password)
        if user is not None:
            return redirect('userlogin')  
        else:
            return render(request, 'create.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'create.html') 
    
def logout_view(request):
    logout(request)
    return redirect('userlogin')  
def index(request):
    return render(request,"index.html")        

