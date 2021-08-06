from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
# Create your views here.

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']

        user=User.objects.create_user(first_name=first_name,username=username,email=email,password=password,last_name=last_name)
        user.save();
        print('aay');
        return redirect('/');

    else:
        return render(request,'register.html')
        


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')




    else:
        return render(request,'login.html')     
