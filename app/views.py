from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *

def StudentForm(request):
    form=Student()
    if request.method=="POST":
        form_data=Student(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))
    return render(request,'student.html',context={'form':form})