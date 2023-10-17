import re
import sys
import datetime
import requests
import time, os, tarfile
import openpyxl
import pyodbc

"""

"""


def handleQuoteFile(filename):
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=172.17.0.239,1433;'
                          'Database=AIS20230524185151;'
                          'Uid=sa;'
                          'PWD=xqerp!@#2023;'
                          'Trusted_Connection=no;'
                          'TDS_Version=8.0')
    cursor = conn.cursor()

    sql_detail = '''
    
    SELECT TOP 1 material_l.*,  material.FNUMBER, materialpurchase.FMINPRICE,  materialpurchase.FMAXPRICE, supplier_l.FNAME AS sFNAME
      FROM dbo.T_BD_MATERIAL_L AS material_l 
    INNER JOIN dbo.T_BD_MATERIALPURCHASE AS materialpurchase ON materialpurchase.FMATERIALID = material_l.FMATERIALID
    INNER JOIN dbo.T_BD_MATERIAL AS material ON material.FMATERIALID = material_l.FMATERIALID

    INNER JOIN dbo.T_PUR_POORDERENTRY as poorderentry ON poorderentry.FMATERIALID = material_l.FMATERIALID
    INNER JOIN dbo.T_PUR_POORDER AS pur_poorder ON pur_poorder.FID = poorderentry.FID
    INNER JOIN dbo.T_BD_SUPPLIER AS supplier ON supplier.FSUPPLIERID = pur_poorder.FSUPPLIERID
    INNER JOIN dbo.T_BD_SUPPLIER_L AS supplier_l ON supplier_l.FSUPPLIERID = supplier.FSUPPLIERID

    WHERE material_l.FSPECIFICATION = ? ;
    
    '''

    print("开始处理excel文件"+filename)
    xheaders = u'FPKID,FMATARIALID,物料名称,规格型号,料号,最高价格,最低价格,供应商,购买次数'.split(',')
    xls_lines = [xheaders]


    file_name = filename
    refer_excel = openpyxl.load_workbook(file_name)
    #获取第一个sheet表格
    sheet1 = refer_excel['sheet']
    material_list = []
    for row in range(2, sheet1.max_row + 1):
        material_list.append({
            "name": (sheet1.cell(row=row, column=1)).value,
            "number": (sheet1.cell(row=row, column=2)).value,
        })

    for material in material_list:
        #print(material["name"])
        number = material["number"]

        rec = cursor.execute(sql_detail, number)
        datalist = rec.fetchall()
        if len(datalist) > 0:
            for line in datalist:
                xls_lines.append([line.FPKID,line.FMATERIALID,line.FNAME,number,line.FNUMBER,line.FMAXPRICE,line.FMINPRICE,line.sFNAME])
        else:
            xls_lines.append(["","",material["name"],number,"","","","",""])

    wb = openpyxl.Workbook()
    ws = wb.active
    for line in xls_lines:
        ws.append(line)
    wb.save("/opt/excel/out_price.xlsx")

    cursor.close()
    conn.close()



