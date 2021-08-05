from travello.models import Destination
from django.shortcuts import render

# Create your views here.



def index(request):
    dests=Destination.objects.all
  
    return render(request,'index.html',{'dests':dests});
