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
      {'title': 'FID', 'width': 90, 'key': 'FID'}
      ,
      {'title': '项目名称', 'width': 90, 'key': 'FNUMBER'}
      ,
      {'title': '创建日期', 'width': 90, 'key': 'FCREATEDATE'}
      ,
      {'title': '客户', 'width': 90, 'key': 'F_XQZD_TEXT'}
    ]
  }
}
