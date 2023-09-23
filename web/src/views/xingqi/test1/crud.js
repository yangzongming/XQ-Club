import { request } from '@/api/service'
export const crudOptions = (vm) => {
  return {
    pageOptions: {
      compact: true
    },
    options: {
      height: '100%'
    },
    viewOptions: {
      componentType: 'row'
    },
    formOptions: {
      defaultSpan: 12 // 默认的表单 span
    },
    columns: [
      {'title': '[采购申请]单号', 'width': 90, 'key': '1'}
      ,
      {'title': '[采购申请]归属项目', 'width': 90, 'key': '2'}
      ,
      {'title': '[采购申请]申请人', 'width': 90, 'key': '3'}
      ,
      {'title': '[采购申请]单据状态', 'width': 90, 'key': '4'}
      ,
      {'title': '[采购申请]创建日期', 'width': 90, 'key': '5'}
      ,
      {'title': '[采购申请]审核日期', 'width': 90, 'key': '6'}
      ,
      {'title': '[采购申请]申请日期', 'width': 90, 'key': '7'}
      ,
      {'title': '[采购申请]单据类型', 'width': 90, 'key': '8'}
      ,
      {'title': '[采购申请]物料ID', 'width': 90, 'key': '9'}
      ,
      {'title': '[采购申请]物料编码', 'width': 90, 'key': '10'}
      ,
      {'title': '[采购申请]物料名称', 'width': 90, 'key': '11'}
      ,
      {'title': '[采购申请]规格型号', 'width': 90, 'key': '12'}
      ,
      {'title': '[采购申请]申请数量', 'width': 90, 'key': '13'}
      ,
      {'title': '[采购申请]批准数量', 'width': 90, 'key': '14'}
      ,
      {'title': '[采购申请]行业务关闭', 'width': 90, 'key': '15'}
      ,
      {'title': '[采购申请]要求到货日期', 'width': 90, 'key': '16'}
      ,
      {'title': '[采购申请]剩余数量', 'width': 90, 'key': '17'}
      ,
      {'title': '[采购申请]订单数量', 'width': 90, 'key': '18'}
      ,
      {'title': '[采购申请]入库数量（几本单位）', 'width': 90, 'key': '19'}
      ,
      {'title': '[采购申请]收料数量（几本单位）', 'width': 90, 'key': '20'}
      ,
      {'title': '[采购订单]编号', 'width': 90, 'key': '21'}
      ,
      {'title': '[采购订单]单据状态', 'width': 90, 'key': '22'}
      ,
      {'title': '[采购订单]采购日期', 'width': 90, 'key': '23'}
      ,
      {'title': '[采购订单]供应商', 'width': 90, 'key': '24'}
      ,
      {'title': '[采购订单]创建人', 'width': 90, 'key': '25'}
      ,
      {'title': '[采购订单]创建日期', 'width': 90, 'key': '26'}
      ,
      {'title': '[采购订单]审核日期', 'width': 90, 'key': '27'}
      ,
      {'title': '[采购订单]采购员', 'width': 90, 'key': '28'}
      ,
      {'title': '[采购订单]单据类型', 'width': 90, 'key': '29'}
      ,
      {'title': '[采购订单]确认日期', 'width': 90, 'key': '30'}
      ,
      {'title': '[采购订单]ID', 'width': 90, 'key': '31'}
      ,
      {'title': '[采购订单]采购数量', 'width': 90, 'key': '32'}
      ,
      {'title': '[采购订单]行业务关闭', 'width': 90, 'key': '33'}
      ,
      {'title': '[采购订单]要求交货日期', 'width': 90, 'key': '34'}
      ,
      {'title': '[采购订单]供应商承诺日期', 'width': 90, 'key': '35'}
      ,
      {'title': '[采购订单]累计收料数量', 'width': 90, 'key': '36'}
      ,
      {'title': '[采购订单]累计入库数量', 'width': 90, 'key': '37'}
      ,
      {'title': '[采购订单]剩余收料数量', 'width': 90, 'key': '38'}
      ,
      {'title': '[采购订单]剩余入库数量', 'width': 90, 'key': '39'}
      ,
      {'title': '[采购订单]源单类型', 'width': 90, 'key': '40'}
      ,
      {'title': '[采购订单]原单编号', 'width': 90, 'key': '41'}
      ,
      {'title': '[采购订单]需求来源', 'width': 90, 'key': '42'}
      ,
      {'title': '[采购订单]需求单据编号', 'width': 90, 'key': '43'}
      ,
      {'title': '[采购订单]需求单据行号', 'width': 90, 'key': '44'}
      ,
      {'title': '[采购订单]需求单据分录内码', 'width': 90, 'key': '45'}
      ,
      {'title': '[收料通知单]编号', 'width': 90, 'key': '46'}
      ,
      {'title': '[收料通知单]单据状态', 'width': 90, 'key': '47'}
      ,
      {'title': '[收料通知单]创建人', 'width': 90, 'key': '48'}
      ,
      {'title': '[收料通知单]创建日期', 'width': 90, 'key': '49'}
      ,
      {'title': '[收料通知单]审核日期', 'width': 90, 'key': '50'}
      ,
      {'title': '[收料通知单]审核人', 'width': 90, 'key': '51'}
      ,
      {'title': '[收料通知单]ID', 'width': 90, 'key': '52'}
      ,
      {'title': '[收料通知单]物料ID', 'width': 90, 'key': '53'}
      ,
      {'title': '[收料通知单]本次交货数量', 'width': 90, 'key': '54'}
      ,
      {'title': '[收料通知单]实到数量', 'width': 90, 'key': '55'}
      ,
      {'title': '[收料通知单]订单单号', 'width': 90, 'key': '56'}
      ,
      {'title': '[收料通知单]原单内码', 'width': 90, 'key': '57'}
      ,
      {'title': '[收料通知单]原单分录内码', 'width': 90, 'key': '58'}
      ,
      {'title': '[收料通知单]原单单号', 'width': 90, 'key': '59'}
      ,
      {'title': '[收料通知单]实收数量', 'width': 90, 'key': '60'}
      ,
      {'title': '[收料通知单]预计到货日期', 'width': 90, 'key': '61'}
      ,
      {'title': '[收料通知单]采购订单分录代码', 'width': 90, 'key': '62'}
      ,
      {'title': '[收料通知单]确认交货数量', 'width': 90, 'key': '63'}
      ,
      {'title': '[收料通知单]确认到货日期', 'width': 90, 'key': '64'}
      ,
      {'title': '[检验单]单号', 'width': 90, 'key': '65'}
      ,
      {'title': '[检验单]单据状态', 'width': 90, 'key': '66'}
      ,
      {'title': '[检验单]审核人', 'width': 90, 'key': '67'}
      ,
      {'title': '[检验单]审核日期', 'width': 90, 'key': '68'}
      ,
      {'title': '[检验单]创建人', 'width': 90, 'key': '69'}
      ,
      {'title': '[检验单]创建日期', 'width': 90, 'key': '70'}
      ,
      {'title': '[检验单]单据日期', 'width': 90, 'key': '71'}
      ,
      {'title': '[检验单]检验数量', 'width': 90, 'key': '72'}
      ,
      {'title': '[检验单]质检开始日期', 'width': 90, 'key': '73'}
      ,
      {'title': '[检验单]质检结束日期', 'width': 90, 'key': '74'}
      ,
      {'title': '[检验单]物料编码ID', 'width': 90, 'key': '75'}
      ,
      {'title': '[检验单]原单类型', 'width': 90, 'key': '76'}
      ,
      {'title': '[检验单]原单编号', 'width': 90, 'key': '77'}
      ,
      {'title': '[检验单]原单内码', 'width': 90, 'key': '78'}
      ,
      {'title': '[检验单]原单分录内码', 'width': 90, 'key': '79'}
      ,
      {'title': '[检验单]原单行号', 'width': 90, 'key': '80'}
      ,
      {'title': '[采购入库]单号', 'width': 90, 'key': '81'}
      ,
      {'title': '[采购入库]单据状态', 'width': 90, 'key': '82'}
      ,
      {'title': '[采购入库]入库日期', 'width': 90, 'key': '83'}
      ,
      {'title': '[采购入库]单据类型', 'width': 90, 'key': '84'}
      ,
      {'title': '[采购入库]供应商', 'width': 90, 'key': '85'}
      ,
      {'title': '[采购入库]创建人', 'width': 90, 'key': '86'}
      ,
      {'title': '[采购入库]创建日期', 'width': 90, 'key': '87'}
      ,
      {'title': '[采购入库]审核人', 'width': 90, 'key': '88'}
      ,
      {'title': '[采购入库]审核日期', 'width': 90, 'key': '89'}
      ,
      {'title': '[采购入库]物料编码ID', 'width': 90, 'key': '90'}
      ,
      {'title': '[采购入库]应收数量', 'width': 90, 'key': '91'}
      ,
      {'title': '[采购入库]实收数量', 'width': 90, 'key': '92'}
      ,
      {'title': '[采购入库]原单行内码', 'width': 90, 'key': '93'}
      ,
      {'title': '[采购入库]订单单号', 'width': 90, 'key': '94'}
      ,
      {'title': '[采购入库]原单类型', 'width': 90, 'key': '95'}
      ,
      {'title': '[采购入库]原单编码', 'width': 90, 'key': '96'}
    ]
  }
}
