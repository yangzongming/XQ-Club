SELECT
	* 
FROM
	(
	SELECT
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
	AND STKIE.[【采购入库】物料编码ID] = purrey.[【收料通知单】物料ID]