from django.shortcuts import render

# Create your views here.

def view_home(request):
    resp=render(request, 'app/home.html')
    return resp
