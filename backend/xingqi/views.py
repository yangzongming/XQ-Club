from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse('星奇科技测试代码---Leo Hello World! I am django～')
