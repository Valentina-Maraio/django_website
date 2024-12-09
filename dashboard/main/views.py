from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(response):
    return HttpResponse("Home Page")

def about(response):
    return HttpResponse("About Page")

