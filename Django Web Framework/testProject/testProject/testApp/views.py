from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('Welcome to Little Lemon Restaurant')
# Create your views here.   
