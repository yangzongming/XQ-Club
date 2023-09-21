from django.http import HttpResponse
from django.shortcuts import render
import json



def index(request):
    html = '<h1>星奇测试------ Leo Hello World， I am Django。</h1>'
    return HttpResponse(html, status=200)

def testJson(request):
    data = {'name': 'John', 'age': 25}
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')