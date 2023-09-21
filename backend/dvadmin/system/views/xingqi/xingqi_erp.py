from django.http import HttpResponse
from django.shortcuts import render
import json
from .check import request_verify


def index(request):
    html = '<h1>星奇测试------ Leo Hello World， I am Django。</h1>'
    return HttpResponse(html, status=200)

@request_verify('get')
def testJson(request):
    data = {'name': 'John', 'age': 25}
    json_data = json.dumps(data)
    return response_page_success(message="成功了",data = json_data)




def response_success(message, data=None, data_list=[]):
    return HttpResponse(json.dumps({
        'code': 200,  # code由前后端配合指定
        'message': message,  # 提示信息
        'data': data,  # 返回单个对象
        'dataList': data_list  # 返回对象数组
    }, ensure_ascii=False), 'application/json')


def response_page_success(message, data=None, data_list=[], total=None, page=None, pageSize=None):
    return HttpResponse(json.dumps({
        'code': 200,  # code由前后端配合指定
        'message': message,  # 提示信息
        'data': data,  # 返回单个对象
        'dataList': data_list,  # 返回对象数组
        'total': total,  # 记录总数
        'page': page,  # 当前页面
        'pageSize': pageSize  # 当前页面分页大小
    }, ensure_ascii=False), 'application/json')