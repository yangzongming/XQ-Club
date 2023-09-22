import { request } from '@/api/service'
import { requestForMock } from '@/api/service'

const urlPre = '/api/system/xingqi'

export function GetList (query) {
  return requestForMock({
    url: urlPre + '/testJson?fid=CGSQ000206',
    method: 'get',
    params: query
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
