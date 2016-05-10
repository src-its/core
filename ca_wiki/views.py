from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the CA Wiki. Here's some text while we \
            figure out how to serve a page.")
    
