from django.shortcuts import render , HttpResponse
from HomePage.models import Courses

# Create your views here.

def details(request):
    obj = Courses.objects.all()
    return render(request,'courses.html',{'obj' : obj})


