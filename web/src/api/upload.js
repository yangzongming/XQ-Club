/**
 * “上传文件”相关接口
 */
import { request } from '@/api/service'
import { serviceForOutside } from '@/api/service'

const urlPre = 'http://172.17.1.249:9602/api/system/xingqi'

export default {
  uploadFile (file) {
  let formData = new FormData()
  formData.append('files', file)
  const config = {
    headers: { "Content-Type": "multipart/form-data;boundary="+new Date().getTime() }
  };
  let service = serviceForOutside()
  service.post("/file/upload",formData,config).then(
    function (response) {
      console.log(response);
    }).catch(function(error) {
    // 上传失败后的处理
    console.error('上传失败', error);
  })
  }
}
