from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    html = '<h1>Hello World</h1>'
    return HttpResponse(html, status=200)