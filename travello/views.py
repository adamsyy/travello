from travello.models import Destination
from django.shortcuts import render

# Create your views here.



def index(request):
    dest1=Destination();
    dest1.name='mumbai'
    dest1.price=200
    dest1.desc="nice aahne"
    dest1.img="destination_1.jpg"
    dest1.offer=False

    dest2=Destination();
    dest2.name='thiruvalla'
    dest2.price=400
    dest2.desc="level aahne"
    dest2.img="destination_2.jpg"
    dest2.offer=True

    dest3=Destination();
    dest3.name='kollam'
    dest3.price=355
    dest3.desc="bad aahne hehe"
    dest3.img="destination_3.jpg"
    dest3.offer=False

    dests=[dest1,dest2,dest3]
    return render(request,'index.html',{'dests':dests});
