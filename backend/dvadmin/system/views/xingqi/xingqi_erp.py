import re
import sys
import datetime
import requests
import time, os, tarfile
import openpyxl
import pyodbc

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
    dlist = craw_requestion_detail('123456')
    return response_page_success(message="成功了",data = json_data, data_list=dlist)

#获取采购申请表明细
def craw_requestion_detail(fid):
    #操作Excel
    file_name = "/opt/excel/price.xlsx"
    refer_excel = openpyxl.load_workbook(file_name)
    sheet1 = refer_excel['比价表']

    # 定义一个请购单数据dic
    pr_dic = {}
    pr_dic['no'] = fid  # 请购单号
    pr_dic['request_date'] = '2023-08-26'  # 请购日期
    pr_dic['request_person'] = 'leo yang'  # 请购人员
    pr_dic['pr_project'] = 'H2-天一阁'
    pr_dic['items'] = []

    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=172.17.0.239,1433;'
                          'Database=AIS20230524185151;'
                          'Uid=sa;'
                          'PWD=xqerp!@#2023;'
                          'Trusted_Connection=no;'
                          'TDS_Version=8.0')
    cursor = conn.cursor()
    sql = ''' SELECT * FROM dbo.T_PUR_REQUISITION AS pur_requesition WHERE pur_requesition.FBILLNO = ?  '''
    recSet = cursor.execute(sql,fid)

    # 处理料号
    limit = 6
    row_number = 0
    for one in recSet:
        #print(str(one.FID))
        #print(str(one.FBILLNO))
        #print(str(one.FAPPROVEDATE))
        FBILLNO = str(one.FBILLNO)
        sql_detail = ''' SELECT pur_requestion.FID,   
                         material.FMATERIALID,material.F_XQZD_TEXT2,material.F_XQZD_TZBB, material_l.FSPECIFICATION, 
                         material_l.FNAME,material.FNUMBER, reqentry.FAPPROVEQTY ,
                         materialpurchase.FMINPRICE,materialpurchase.FMAXPRICE 
                         FROM dbo.T_PUR_REQUISITION AS pur_requestion 
                         INNER JOIN dbo.T_PUR_REQENTRY AS reqentry on pur_requestion.FID = reqentry.FID
                         INNER JOIN dbo.T_BD_MATERIAL AS material ON reqentry.FMATERIALID = material.FMATERIALID
                         INNER JOIN dbo.T_BD_MATERIAL_L AS material_l ON material_l.FMATERIALID = material.FMATERIALID
                         INNER JOIN dbo.T_BD_MATERIALPURCHASE AS materialpurchase ON materialpurchase.FMATERIALID = material.FMATERIALID
                         WHERE pur_requestion.FBILLNO = ?
                         ORDER BY pur_requestion.FCREATEDATE; '''
        rec = cursor.execute(sql_detail, FBILLNO)
        list = rec.fetchall()
        sheet1.insert_rows(7, len(list))
        for line in list:
            sheet1['A' + str(limit + row_number)] = row_number + 1
            sheet1['B' + str(limit + row_number)] = pr_dic['pr_project']
            sheet1['C' + str(limit + row_number)] = line.FNUMBER
            sheet1['D' + str(limit + row_number)] = line.FNAME
            sheet1['F' + str(limit + row_number)] = line.FSPECIFICATION
            sheet1['G' + str(limit + row_number)] = line.FAPPROVEQTY
            sheet1['H' + str(limit + row_number)] = line.FMAXPRICE
            sheet1['I' + str(limit + row_number)] = line.FMINPRICE
            row_number += 1
    #写数据
    sheet1['A3'] = u'采购申请单编号：' + pr_dic['no']
    sheet1['R3'] = u'期望交期' + pr_dic['request_date']
    refer_excel.save( "/opt/excel/" + fid + '.xlsx')
    return list


#封装请求
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