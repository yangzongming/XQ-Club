import { request } from '@/api/service'
import { requestForOutside } from '@/api/service'

const urlPre = 'http://172.17.1.249:9602/api/system/xingqi'

export function GetList (query) {
  return requestForOutside({
    url: urlPre + '/get_purcharse_track_detail',
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
