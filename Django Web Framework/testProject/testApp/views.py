from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #print(dir(request))
    print(request)
    #print(request.content_params)
    return HttpResponse('Welcome to Little Lemon Restaurant')
# Create your views here.   
