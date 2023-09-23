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
      {
        title: '编码',
        key: 'A',
        width: 90
      },
      {
        title: '看法',
        key: 'B',
        width: 90
      },
      {
        title: '什么',
        key: 'C',
        width: 90
      },
      {
        title: '编码',
        key: 'D',
        width: 90
      }
    ]
  }
}
