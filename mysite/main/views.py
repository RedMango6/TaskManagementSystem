from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<h1>tech with tim</h1>")   #will return HTML 5 code

def v1(response):
    return HttpResponse("<h1> view 1! </h1>")