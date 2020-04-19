from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from lecture.models import *
from department.models import *
from ads.models import *


# Create your views here.
#def index(request,):
    #return render(request,"index.html")#
#def classno(request,slug):
#    return render(request,"about.html")#

def classpick(request):
    classes = Classroom.objects.all()
    context = {
        'class':classes
    }
    
    return render(request,'index.html',context)

def about(request,pk_test):
    classes = Classroom.objects.get(classroom_name=pk_test)
    department = Department.objects.all()
    ads= Ads.objects.all()
    context = {'classes':classes,'department':department,'ads':ads}
    return render(request,'about.html',context)

    

