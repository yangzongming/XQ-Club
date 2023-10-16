/**
 * “上传文件”相关接口
 */
import {uploadFile, request, requestForOutside} from '@/api/service'
//import { requestForOutsideSELF } from '@/api/service'
import axios from 'axios'
import util from '@/libs/util'
import {urlPrefix} from "@/views/system/user/api";

const urlPre = 'http://172.17.1.249:9602/api/system/xingqi'

export default {
  uploadFile (file) {
    let formData = new FormData()
    console.log(file)
    formData.append('file', file)
    axios.post(urlPre + "upload_file", formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      })
  }
}
