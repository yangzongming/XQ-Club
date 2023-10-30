import re
import sys
import datetime
import requests
import time, os, tarfile
import openpyxl
import pyodbc


from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import json
from .check import request_verify
from dvadmin.utils.DateEncode import DateEncoder
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .util.QuoteUtil import handleQuoteFile, handleMaterialPrice, saveMaterialPriceList, saveMaterialPriceSummary

#from dvadmin.system.views.xingqi.models.User import User, session
from dvadmin.system.views.xingqi.models.Material import Material, session

def index(request):
    html = '<h1>星奇测试------ Leo Hello World， I am Django。</h1>'
    return HttpResponse(html, status=200)

def testJson(request):
    material = Material(material_number="UJR-6.35MS-L28-AW", material_name=u'1/4VCR短格兰L28', material_brand="FUJIKIN", info="没有描述")
    session.add(material)
    session.commit()
    r1 = session.query(Material).filter(Material.material_number == "UJR-6.35MS-L28-AW").all()
    print(r1)
    return response_page_success(message="成功了", data="", total=100, limit= 10, page= 1)

def get_purcharse_track_detail(request):
    dic = craw_purcharse_detail()
    return response_page_success(message="成功了", data=dic["data"], total=dic["total"], limit= dic["limit"], page= dic["page"])

def get_project_list(request):
    dic = craw_projectlist();
    return response_page_success(message="成功了", data=dic["data"], total=dic["total"], limit=dic["limit"],
                                 page=dic["page"])

@csrf_exempt
def save_material_price_summary(request):
    if request.method == 'POST':
        #存储数据吧
        jsonData = json.loads(request.body)
        if jsonData == None:
            return JsonResponse({"code": 1}, safe=False)
        else:
            saveMaterialPriceSummary(jsonData)
            return JsonResponse({"code": 0}, safe=False)
    else:
        return JsonResponse({"code": 1, 'errmsg': '使用POST方法'}, safe=False)

@csrf_exempt
def material_price_update(request):
    if request.method == 'POST':
        #处理数据吧
        jsonData = json.loads(request.body)
        #print(jsonData)
        saveMaterialPriceList(jsonData)
        return JsonResponse({"code": 0}, safe=False)


#处理星奇-Club报价上传文件
@csrf_exempt
def upload_material_price_file(request):
    if request.method == 'POST':
        file = request.FILES.get("file")
        if file:
            filePath = os.path.join(settings.EXCEL_ROOT, file.name)
            with open(filePath, 'wb+') as fp:
                for info in file.chunks():
                    fp.write(info)
                    fp.close()
            #文件在服务端路径 获取配置
            #保存好文件后，处理报价并发送邮件给supplier@xingqikeji.com
            dataInfo = handleMaterialPrice(filePath)
            if dataInfo['code'] == 0:
                return JsonResponse(dataInfo, safe=False)
            else:
                return JsonResponse('失败了，报价文件已经提交过了', safe=False)
        else:
            return JsonResponse('失败了，文件错误', safe=False)
    else:
        return JsonResponse('请选择POST提交文件！', safe=False)

#上传星奇ERP的询价文件
@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        file = request.FILES.get("file")
        if file:
            filePath = os.path.join(settings.EXCEL_ROOT, file.name)
            with open(filePath, 'wb+') as fp:
                for info in file.chunks():
                    fp.write(info)
                    #print(info)
            # 文件在服务端路径 获取配置
            # 保存好文件后，处理报价并发送邮件给supplier@xingqikeji.com
            handleQuoteFile(filePath)

            return HttpResponse('上传成功！')
        else:
            return HttpResponse('失败了，文件错误')
    else:
        return HttpResponse('请选择POST提交文件！')

def craw_projectlist():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=172.17.0.239,1433;'
                          'Database=AIS20230524185151;'
                          'Uid=sa;'
                          'PWD=xqerp!@#2023;'
                          'Trusted_Connection=no;'
                          'TDS_Version=8.0')
    cursor = conn.cursor()
    sql = """ SELECT bas_predbtwo.FID,bas_predbtwo.FNUMBER,bas_predbtwo.FCREATEDATE,bas_predbtwo.F_XQZD_TEXT
     FROM dbo.T_BAS_PREBDTWO as bas_predbtwo ORDER BY bas_predbtwo.FCREATEDATE DESC """
    recSet = cursor.execute(sql)
    datalist = recSet.fetchall()
    xls_lines = []
    for line in datalist:
        xls_lines.append({
            'FID': line[0],
            'FNUMBER': line[1],
            'FCREATEDATE': line[2],
            'F_XQZD_TEXT': line[3]
        })

    tmp_lines = xls_lines[: 500]
    return {
        "data": tmp_lines,
        "total": len(tmp_lines),
        "limit": 50,
        "page": 1,
    }

def craw_purcharse_detail():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=172.17.0.239,1433;'
                          'Database=AIS20230524185151;'
                          'Uid=sa;'
                          'PWD=xqerp!@#2023;'
                          'Trusted_Connection=no;'
                          'TDS_Version=8.0')
    cursor = conn.cursor()
    sql = """ SELECT * FROM (SELECT
		purr.FBILLNO AS "【采购申请】单号",
		BASL.FNAME AS "【采购申请】归属项目",
		emp.FNAME AS "【采购申请】申请人",
		purr.FDocumentStatus AS "【采购申请】单据状态",
		purr.FCreateDate AS "【采购申请】创建日期",
		purr.FApproveDate AS "【采购申请】审核日期",
		purr.FApplicationDate AS "【采购申请】申请日期",
		purr.FBillTypeID AS "【采购申请】单据类型",
		BDM.FMaterialId AS "【采购申请】物料ID",
		bdm.fnumber AS "【采购申请】物料编码",
		BDM.fname AS "【采购申请】物料名称",
		BDM.FSpecification AS "【采购申请】规格型号",
		pure.FReqQty AS "【采购申请】申请数量",
		pure.FApproveQty AS "【采购申请】批准数量",
		pure.FMRPCloseStatus AS "【采购申请】行业务关闭",
		pure.FArrivalDate AS "【采购申请】要求到货日期",
		purer.FRemainQty AS "【采购申请】剩余数量",
		purer.FOrderQty AS "【采购申请】订单数量",
		purer.FBaseStockQty AS "【采购申请】入库数量(基本单位)",
		purer.FBaseReceiveQty AS "【采购申请】收料数量(基本单位)" 
	    FROM
		T_PUR_REQENTRY AS pure
		LEFT JOIN T_PUR_REQUISITION AS purr ON purr.fid  = pure.fid
		LEFT JOIN T_PUR_REQENTRY_R AS purer ON pure.fentryid = purer.fentryid
		LEFT JOIN T_BAS_PREBDTWO_L AS BASL ON purr.F_XQZD_Base = BASL.FID
		LEFT JOIN (
		SELECT
			BDM.FMaterialId,
			BDM.fnumber ,
			BDML.fname ,
			BDML.FSpecification 
		FROM
			T_BD_MATERIAL AS BDM
			LEFT JOIN T_BD_MATERIAL_L AS BDML ON BDM.FMATERIALID = BDML.FMATERIALID 
		) AS BDM ON pure.FMaterialId = BDM.FMaterialId
		LEFT JOIN (
		SELECT
			BDS.FSTAFFID ,
			EMP.FNUMBER ,
			EMPL.FNAME 
		FROM
			T_HR_EMPINFO AS EMP
			LEFT JOIN T_HR_EMPINFO_L AS EMPL ON EMP.fid = EMPL.fid
			LEFT JOIN T_BD_STAFF AS BDS ON BDS.FNUMBER = EMP.FNUMBER 
		) EMP ON emp.FSTAFFID = purr.FAPPLICANTID 
	    WHERE
		purr.FApplicationDate > '2023-7-31' 
	    ) pure
	    LEFT JOIN (
	    SELECT
		purp.FBillNo AS "【采购订单】编号",
		purp.FDocumentStatus AS "【采购订单】单据状态",
		purp.FDate AS "【采购订单】采购日期",
		purp.FSupplierId AS "【采购订单】供应商",
		purp.FCreatorId AS "【采购订单】创建人",
		purp.FCreateDate AS "【采购订单】创建日期",
		purp.FApproveDate AS "【采购订单】审核日期",
		purp.FPurchaserId AS "【采购订单】采购员",
		purp.FBillTypeID AS "【采购订单】单据类型",
		purp.FConfirmDate AS "【采购订单】确认日期",
		purpe.FENTRYID AS "【采购订单】ID",
		purpe.FMaterialId AS "【采购订单】物料ID",
		purpe.FBaseUnitQty AS "【采购订单】采购基本数量",
		purpe.FMRPCloseStatus AS "【采购订单】行业务关闭",
		purpe.F_XQZD_Date1 AS "【采购订单】要求的交货日期",
		purped.FDeliveryDate AS "【采购订单】供应商承诺日期",
		purper.FReceiveQty AS "【采购订单】累计收料数量",
		purper.FStockInQty AS "【采购订单】累计入库数量",
		purper.FRemainReceiveQty AS "【采购订单】剩余收料数量",
		purper.FRemainStockINQty AS "【采购订单】剩余入库数量",
		purper.FSrcBillTypeId AS "【采购订单】源单类型",
		purper.FSrcBillNo AS "【采购订单】源单编号",
		purper.FDEMANDTYPE AS "【采购订单】需求来源",
		purper.FDEMANDBILLNO AS "【采购订单】需求单据编号",
		purper.FDEMANDBILLENTRYSEQ AS "【采购订单】需求单据行号",
		purper.FDEMANDBILLENTRYID AS "【采购订单】需求单据分录内码" 
	    FROM
		T_PUR_POORDERENTRY purpe
		LEFT JOIN T_PUR_POORDERENTRY_D purped ON purpe.fentryid = purped.fentryid
		LEFT JOIN T_PUR_POORDER AS purp ON purpe.fid = purp.fid
		LEFT JOIN T_PUR_POORDERENTRY_R purper ON purper.fentryid = purpe.fentryid 
	    WHERE
		purper.FSrcBillNo <> '' 
	    ) purp ON pure.[【采购申请】单号] = purp.[【采购订单】源单编号] 
	    AND pure.[【采购申请】物料ID] = purp.[【采购订单】物料ID]
	    LEFT JOIN (
	    SELECT
		purre.FBillNo AS "【收料通知单】编号",
		purre.FDocumentStatus AS "【收料通知单】单据状态",
		purre.FDate AS "【收料通知单】收料日期",
		purre.FCreatorId AS "【收料通知单】创建人",
		purre.FCreateDate AS "【收料通知单】创建日期",
		purre.FApproveDate AS "【收料通知单】审核日期",
		purre.FApproverId AS "【收料通知单】审核人",
		purrey.FENTRYID AS "【收料通知单】ID",
		purrey.FMaterialId AS "【收料通知单】物料ID",
		purrey.FActReceiveQty AS "【收料通知单】本次交货数量",
		purrey.FActlandQty AS "【收料通知单】实到数量",
		purrey.FOrderBillNo AS "【收料通知单】订单单号",
		purrey.FSrcId AS "【收料通知单】源单内码",
		purrey.FSrcEntryId AS "【收料通知单】源单分录内码",
		purrey.FSrcBillNo AS "【收料通知单】源单单号",
		purrey.FMustQty AS "【收料通知单】实收数量",
		purrey.FPreDeliveryDate AS "【收料通知单】预计到货日期",
		purrey.FPOORDERENTRYID AS "【收料通知单】采购订单分录内码",
		purrer.FConfirmDeliQty AS "【收料通知单】确认交货数量",
		purrer.FConfirmDeliDate AS "【收料通知单】确认到货日期" 
	    FROM
		T_PUR_RECEIVEENTRY purrey
		LEFT JOIN T_PUR_RECEIVE purre ON purrey.FID = purre.FID
		LEFT JOIN T_PUR_RECEIVEENTRY_R purrer ON purrey.FENTRYID = purrer.FENTRYID 
	    WHERE
		purre.FCreateDate > '2023-08-01' 
	    ) AS purrey ON purrey.[【收料通知单】源单单号] = purp.[【采购订单】编号] 
	    AND purrey.[【收料通知单】源单分录内码] = purp.[【采购订单】ID]
	    LEFT JOIN (
	    SELECT
		QMI.FBillNo AS "【检验单】单号",
		QMI.FDocumentStatus AS "【检验单】单据状态",
		QMI.FApproverId AS "【检验单】审核人",
		QMI.FApproveDate AS "【检验单】审核日期",
		QMI.FCreatorId AS "【检验单】创建人",
		QMI.FCreateDate AS "【检验单】创建日期",
		QMI.FDate AS "【检验单】单据日期",
		QMIE.FInspectQty AS "【检验单】检验数量",
		QMIE.FInspectStartDate AS "【检验单】质检开始日期",
		QMIE.FInspectEndDate AS "【检验单】质检结束日期",
		QMIEA.FMaterialId AS "【检验单】物料编码ID",
		QMIEA.FSrcBillType AS "【检验单】源单类型",
		QMIEA.FSrcBillNo AS "【检验单】源单编号",
		QMIEA.FSrcInterId AS "【检验单】源单内码",
		QMIEA.FSrcEntryId AS "【检验单】源单分录内码",
		QMIEA.FSrcEntrySeq AS "【检验单】源单行号" 
	    FROM
		T_QM_INSPECTBILLENTRY AS QMIE
		LEFT JOIN T_QM_INSPECTBILL AS QMI ON QMIE.FID = QMI.FID
		LEFT JOIN T_QM_INSPECTBILLENTRY_A AS QMIEA ON QMIE.FENTRYID = QMIEA.FENTRYID 
	    WHERE
		QMI.FCreateDate > '2023-01-01' 
	    ) AS QMIE ON purrey.[【收料通知单】编号] = QMIE.[【检验单】源单编号] 
	    AND purrey.[【收料通知单】ID] = QMIE.[【检验单】源单分录内码]
	    LEFT JOIN (
	    SELECT
		STKI.FBillNo AS "【采购入库】单号",
		STKI.FDocumentStatus AS "【采购入库】单据状态",
		STKI.FDate AS "【采购入库】入库日期",
		STKI.FBillTypeID AS "【采购入库】单据类型",
		STKI.FSupplierId AS "【采购入库】供应商",
		STKI.FCreatorId AS "【采购入库】创建人",
		STKI.FCreateDate AS "【采购入库】创建日期",
		STKI.FApproverId AS "【采购入库】审核人",
		STKI.FApproveDate AS "【采购入库】审核日期",
		STKIE.FMaterialId AS "【采购入库】物料编码ID",
		FMustQty AS "【采购入库】应收数量",
		FRealQty AS "【采购入库】实收数量",
		FSRCRowId AS "【采购入库】源单行内码",
		FPOOrderNo AS "【采购入库】订单单号",
		FSRCBILLTYPEID AS "【采购入库】源单类型",
		FSRCBillNo AS "【采购入库】源单编号" 
	    FROM
		T_STK_INSTOCKENTRY AS STKIE
		LEFT JOIN T_STK_INSTOCK AS STKI ON STKI.FID = STKIE.FID 
	    ) AS STKIE ON STKIE.[【采购入库】源单编号] = purrey.[【收料通知单】编号] 
	    AND STKIE.[【采购入库】物料编码ID] = purrey.[【收料通知单】物料ID] """
    recSet = cursor.execute(sql)
    datalist = recSet.fetchall()
    xls_lines = []
    for line in datalist:
        xls_lines.append({
            '[采购申请]单号': line[0],
            '[采购申请]归属项目': line[1],
            '[采购申请]申请人': line[2],
            '[采购申请]单据状态': line[3],
            '[采购申请]创建日期': line[4],
            '[采购申请]审核日期': line[5],
            '[采购申请]申请日期': line[6],
            '[采购申请]单据类型': line[7],
            '[采购申请]物料ID': line[8],
            '[采购申请]物料编码': line[9],
            '[采购申请]物料名称': line[10],
            '[采购申请]规格型号': line[11],
            '[采购申请]申请数量': line[12],
            '[采购申请]批准数量': line[13],
            '[采购申请]行业务关闭': line[14],
            '[采购申请]要求到货日期': line[15],
            '[采购申请]剩余数量': line[16],
            '[采购申请]订单数量': line[17],
            '[采购申请]入库数量（几本单位）': line[18],
            '[采购申请]收料数量（几本单位）': line[19],
            '[采购订单]编号': line[20],
            '[采购订单]单据状态': line[21],
            '[采购订单]采购日期': line[22],
            '[采购订单]供应商': line[23],
            '[采购订单]创建人': line[24],
            '[采购订单]创建日期': line[25],
            '[采购订单]审核日期': line[26],
            '[采购订单]采购员': line[27],
            '[采购订单]单据类型': line[28],
            '[采购订单]确认日期': line[29],
            '[采购订单]ID': line[30],
            '[采购订单]采购数量': line[31],
            '[采购订单]行业务关闭': line[32],
            '[采购订单]要求交货日期': line[33],
            '[采购订单]供应商承诺日期': line[34],
            '[采购订单]累计收料数量': line[35],
            '[采购订单]累计入库数量': line[36],
            '[采购订单]剩余收料数量': line[37],
            '[采购订单]剩余入库数量': line[38],
            '[采购订单]源单类型': line[39],
            '[采购订单]原单编号': line[40],
            '[采购订单]需求来源': line[41],
            '[采购订单]需求单据编号': line[42],
            '[采购订单]需求单据行号': line[43],
            '[采购订单]需求单据分录内码': line[44],
            '[收料通知单]编号': line[45],
            '[收料通知单]单据状态': line[46],
            '[收料通知单]创建人': line[47],
            '[收料通知单]创建日期': line[48],
            '[收料通知单]审核日期': line[49],
            '[收料通知单]审核人': line[50],
            '[收料通知单]ID': line[51],
            '[收料通知单]物料ID': line[52],
            '[收料通知单]本次交货数量': line[53],
            '[收料通知单]实到数量': line[54],
            '[收料通知单]订单单号': line[55],
            '[收料通知单]原单内码': line[56],
            '[收料通知单]原单分录内码': line[57],
            '[收料通知单]原单单号': line[58],
            '[收料通知单]实收数量': line[59],
            '[收料通知单]预计到货日期': line[60],
            '[收料通知单]采购订单分录代码': line[61],
            '[收料通知单]确认交货数量': line[62],
            '[收料通知单]确认到货日期': line[63],
            '[检验单]单号': line[64],
            '[检验单]单据状态': line[65],
            '[检验单]审核人': line[66],
            '[检验单]审核日期': line[67],
            '[检验单]创建人': line[68],
            '[检验单]创建日期': line[69],
            '[检验单]单据日期': line[70],
            '[检验单]检验数量': line[71],
            '[检验单]质检开始日期': line[72],
            '[检验单]质检结束日期': line[73],
            '[检验单]物料编码ID': line[74],
            '[检验单]原单类型': line[75],
            '[检验单]原单编号': line[76],
            '[检验单]原单内码': line[77],
            '[检验单]原单分录内码': line[78],
            '[检验单]原单行号': line[79],
            '[采购入库]单号': line[80],
            '[采购入库]单据状态': line[81],
            '[采购入库]入库日期': line[82],
            '[采购入库]单据类型': line[83],
            '[采购入库]供应商': line[84],
            '[采购入库]创建人': line[85],
            '[采购入库]创建日期': line[86],
            '[采购入库]审核人': line[87],
            '[采购入库]审核日期': line[88],
            '[采购入库]物料编码ID': line[89],
            '[采购入库]应收数量': line[90],
            '[采购入库]实收数量': line[91],
            '[采购入库]原单行内码': line[92],
            '[采购入库]订单单号': line[93],
            '[采购入库]原单类型': line[94],
            '[采购入库]原单编码': line[95],
        })
    tmp_lines = xls_lines[: 100]
    return {
        "data": tmp_lines,
        "total": len(tmp_lines),
        "limit": 50,
        "page": 1,
    }

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
    xls_lines = []

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
        datalist = rec.fetchall()
        sheet1.insert_rows(7, len(datalist))
        for line in datalist:
            sheet1['A' + str(limit + row_number)] = row_number + 1
            sheet1['B' + str(limit + row_number)] = pr_dic['pr_project']
            sheet1['C' + str(limit + row_number)] = line.FNUMBER
            sheet1['D' + str(limit + row_number)] = line.FNAME
            sheet1['F' + str(limit + row_number)] = line.FSPECIFICATION
            sheet1['G' + str(limit + row_number)] = line.FAPPROVEQTY
            sheet1['H' + str(limit + row_number)] = line.FMAXPRICE
            sheet1['I' + str(limit + row_number)] = line.FMINPRICE
            row_number += 1

            dic = {}
            dic['A'] = row_number + 1
            dic['B'] = pr_dic['pr_project']
            dic['C'] = line.FNUMBER
            dic['D'] = line.FNAME
            xls_lines.append(dic)
    #写数据
    sheet1['A3'] = u'采购申请单编号：' + pr_dic['no']
    sheet1['R3'] = u'期望交期' + pr_dic['request_date']
    refer_excel.save( "/opt/excel/" + fid + '.xlsx')
    return xls_lines


#封装请求
def response_success(message, data=None, data_list=[]):
    return HttpResponse(json.dumps({
        'code': 200,  # code由前后端配合指定
        'msg': message,  # 提示信息
        'data': data,  # 返回单个对象
        'dataList': data_list  # 返回对象数组
    }, ensure_ascii=False), 'application/json')


def response_page_success(message, data=[], total=None, page=None, limit=None):
    return HttpResponse(json.dumps({
        'code': 200,  # code由前后端配合指定
        'msg': message,  # 提示信息
        'data': {
            'page' : page,
            'limit' : limit,
            'total' : total,
            'data' : data,
        },  # 返回单个对象
    }, cls=DateEncoder, ensure_ascii=False), 'application/json')