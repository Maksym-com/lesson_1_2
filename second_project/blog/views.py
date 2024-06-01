from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    menu = ['home', 'about', 'posts']
    return render(request, 'blog/index.html', {'menu': menu})

def about(request):
    return render(request, 'blog/about.html')
