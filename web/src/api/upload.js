/**
 * “上传文件”相关接口
 */
import { request } from '@/api/service'
import { serviceForOutside } from '@/api/service'
import axios from 'axios'

const urlPre = 'http://172.17.1.249:9602/api/system/xingqi'

export default {
  uploadFile (file) {
    let formData = new FormData()
    formData.append('files', file)
    const config = {
      headers: { "Content-Type": "multipart/form-data;boundary="+new Date().getTime() }
    }
    let service = serviceForOutside()
    console.log("fuck")
    console.log(instanceof axios)
    service.post(urlPre + "/file/upload", formData, config)
      .then( response =>{
        console.log('全部响应结果:', response);
      })
  }
}
