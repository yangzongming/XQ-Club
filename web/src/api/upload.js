/**
 * “上传文件”相关接口
 */
import {downloadFile, request, requestForOutside} from '@/api/service'
//import { requestForOutsideSELF } from '@/api/service'
import axios from 'axios'
import util from '@/libs/util'
import {urlPrefix} from "@/views/system/user/api";

const urlPre = 'http://172.17.1.249:9602/api/system/xingqi'

export default {
  uploadFile (file){
    let formData = new FormData()
    formData.append('files', file)
    return downloadFile({
      url: urlPre + '/upload_file',
      method: 'post',
      data: formData
  })}
}
