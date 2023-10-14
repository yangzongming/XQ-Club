/**
 * “上传文件”相关接口
 */
import {request, requestForOutside} from '@/api/service'
import { requestForOutsideSELF } from '@/api/service'
import axios from 'axios'
import util from '@/libs/util'

const urlPre = 'http://172.17.1.249:9602/api/system/xingqi'

export default {
  uploadFile (file) {
    let formData = new FormData()
    formData.append('files', file)
    const token = util.cookies.get('token')
    const config = {
      headers: {
        "Content-Type": "multipart/form-data;boundary="+new Date().getTime(),
        "Authorization": 'JWT ' + token
      }
    }
    const service = requestForOutsideSELF(config)
    let type = Object.prototype.toString.call(service)
    console(type)
    service.post(urlPre + "/upload_file", formData, config)
      .then( response =>{
        console.log('全部响应结果:', response);
      })
  }
}
