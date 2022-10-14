from django.shortcuts import render,redirect
from .models import User
# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        User.objects.create_user(username=username,password=password,phone=phone,address=address)
        return redirect('login/')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        me = User.objects.get(username=username)
        if me.password == password:
            request.session['user']=me.username
            return redirect('/home')
    elif request.method == 'GET':
        return render(request,'login.html')
    
    
def home(request):

    user= request.user.is_authenticated
    if user:
        return render(request,'home.html')
    else:
        return render(request,'login.html')
        # 왜 리다이렉트하면 안되지???