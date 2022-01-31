from django.shortcuts import render
from django.http import HttpResponse

def posts_list(request):
    return HttpResponse('<h1>Hello from posts_list<h1>')
