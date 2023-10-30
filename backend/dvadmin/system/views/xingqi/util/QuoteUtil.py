import re
import sys
import datetime
import requests
import time, os, tarfile
import openpyxl
import pyodbc

from .MailUtil import send_email
from dvadmin.system.views.xingqi.models.Material import Material, session
from dvadmin.system.views.xingqi.models.MaterialPrice import MaterialPrice

#处理报价文件
def handleMaterialPrice(filename):
    file_name = filename
    refer_excel = openpyxl.load_workbook(file_name)
    # 获取第一个sheet表格
    sheet1 = refer_excel['sheet']
    material_list = []
    for row in range(2, sheet1.max_row + 1):
        material_list.append({
            "name": (sheet1.cell(row=row, column=1)).value,
            "number": (sheet1.cell(row=row, column=2)).value,
            "mode": (sheet1.cell(row=row, column=3)).value,
            "brand": (sheet1.cell(row=row, column=4)).value,
            "supplier": (sheet1.cell(row=row, column=5)).value,
            "amount": (sheet1.cell(row=row, column=7)).value,
            "price": (sheet1.cell(row=row, column=8)).value,
        })
    for material in material_list:
        r1 = session.query(Material).filter(Material.material_number == material["number"]).all()
        if len(r1) > 0:
            #说明存在了
            print("这个料存在"+material["number"])
        else:
            m = Material(material_number=material["number"], material_name=material["name"],
                                material_brand=material["brand"], material_mode=material["mode"])
            session.add(m)
            print(m.material_id)
    session.commit()
    #先增加物料信息
    return material_list


def saveMaterialPriceSummary(priceSummaryInfo):
    print(123)

#保存报价信息
def saveMaterialPriceList(list):
    for mPrice in list:
        r1 = session.query(Material).filter(Material.material_number == mPrice["number"]).all()
        if len(r1) > 0:
            print(r1[0].material_number)
            mp = MaterialPrice(price=mPrice["price"],
                               material_id=r1[0].material_id,
                               amount = mPrice["amount"],
                               supplier = mPrice["supplier"])
            session.add(mp)
        else:
            print("FUCK it is none")
    session.commit()


#处理星奇系统里面的报价明细
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
    
    SELECT TOP 100 material_l.*,  material.FNUMBER, materialpurchase.FMINPRICE,  materialpurchase.FMAXPRICE, supplier_l.FNAME AS sFNAME
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
    print(material_list)
    for material in material_list:
        #print(material["name"])
        number = material["number"]
        #print(number)
        rec = cursor.execute(sql_detail, number)
        datalist = rec.fetchall()
        if len(datalist) > 0:
            line = datalist[0]
            print(line)
            xls_lines.append(
                [line.FPKID, line.FMATERIALID, line.FNAME, number, line.FNUMBER, line.FMAXPRICE, line.FMINPRICE,
                 line.sFNAME, len(datalist)])
        else:
            xls_lines.append(["","",material["name"],number,"","","","",""])

    wb = openpyxl.Workbook()
    ws = wb.active
    for line in xls_lines:
        ws.append(line)
    cursor.close()
    conn.close()
    wb.save("/opt/excel/out_price.xlsx")
    send_email("supplier", "/opt/excel/out_price.xlsx")



