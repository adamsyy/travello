from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html',{'name':"appu"});

def add(request):
    val1=int(request.POST['fname'])
    val2=int(request.POST['lname'])   
    res=val2+val1;  
    return render(request,'result.html',{'result':res,'val1':val1});


