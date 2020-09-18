from django.http import HttpResponse
#to render template we need to import it
from django.shortcuts import render
#you need to enter templates folder name in settings.py

def homepage(request):
    #return HttpResponse('Home Page');
    return render(request,'homepage.html')

def about(request):
    #return HttpResponse('about')
    return render(request,'about.html')