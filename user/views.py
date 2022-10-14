from django.shortcuts import render,redirect
from .models import User
from django.contrib.auth import login, authenticate
# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
        
    elif request.method == 'POST':
        user = User()
        user.username = request.POST.get('username')
        user.set_password(request.POST.get('password'))
        user.phone = request.POST.get('phone')
        user.address = request.POST.get('address')

        user.save()
        return redirect('/login/')
        


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/home')
    elif request.method == 'GET':
        return render(request,'login.html')
    
    
def home(request):
    user= request.user.is_authenticated
    if user:
        return render(request,'home.html')
    else:
        return redirect('/login/')
       