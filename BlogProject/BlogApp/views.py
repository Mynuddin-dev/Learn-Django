from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Blog Home Page')

def about(request):
    return HttpResponse('Blog About Page')