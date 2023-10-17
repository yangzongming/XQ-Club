/**
 * “上传文件”相关接口
 */
import axios from 'axios'

const urlPre = 'http://172.17.1.249:9602/api/system/xingqi'

export default {
  uploadFile (file) {
    let formData = new FormData()
    console.log(file)
    formData.append('file', file)
    axios.post(urlPre + "/upload_file", formData, {
        headers: {
          'Content-Type': 'multipart/form-data;charset=UTF-8'
        }
      })
  }
}
