import { request } from '@/api/service'
import { requestForOutside } from '@/api/service'

const urlPre = 'http://172.17.1.249:9602/api/system/xingqi'

export function GetList (query) {
  return requestForOutside({
    url: urlPre + '/testJson?fid=CGSQ000206',
    method: 'get',
    params: query
  }).then(ret=>{
    //在这里改造成crud所需要的结果
    ret.data = ret.data?ret.data : {}
    ret.data.current = 1
    ret.data.size = 10
    ret.data.total = 100
    ret.data.records = ret.dataList
    return ret
  })
}
export function AddObj (obj) {
  return request({
    url: '/select/add',
    method: 'post',
    data: obj
  })
}

export function UpdateObj (obj) {
  return request({
    url: '/select/update',
    method: 'post',
    data: obj
  })
}
export function DelObj (id) {
  return request({
    url: '/select/delete',
    method: 'post',
    data: { id }
  })
}
export function GetCascadeData () {
  return request({
    url: '/select/cascadeData',
    method: 'get'
  })
}
