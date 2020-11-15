from . models import Courses
from django.shortcuts import render,HttpResponse

# Create your views here.

def home(request):
        courses = Courses.objects.order_by('?')[:6]
        return render(request,'index.html', {'cour' : courses})


def search(request):
    query = request.GET['query']
    sear_cour = Courses.objects.filter(cour_name__icontains=query)
    return render(request,'search.html',{'sear_cour' : sear_cour})


