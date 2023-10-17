import re
import sys
import datetime
import requests
import time, os, tarfile
import openpyxl




def handleQuoteFile(filename):
    print("开始处理excel文件")
    file_name = filename
    refer_excel = openpyxl.load_workbook(file_name)
    #获取第一个sheet表格
    sheet1 = refer_excel['sheet']
    brand_model_dict = {}
    for row in range(2, sheet1.max_row + 1):
        brand = (sheet1.cell(row=row, column=1)).value
        model = (sheet1.cell(row=row, column=2)).value
        brand_model_dict[model] = brand
    print('brand_model_dict= ' + str(brand_model_dict))

