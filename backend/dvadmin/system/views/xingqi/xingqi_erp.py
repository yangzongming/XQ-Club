from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    html = '<h1>星奇测试------ Leo Hello World， I am Django。</h1>'
    return HttpResponse(html, status=200)