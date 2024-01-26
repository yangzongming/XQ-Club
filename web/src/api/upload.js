/**
 * “上传文件”相关接口
 */
import axios from 'axios'
import util from "@/libs/util";

const urlPre = 'http://172.17.1.249:9602/api/system/xingqi'

export default {
  uploadFile (file) {
    const formData = new FormData()
    console.log(util.cookies.get('uuid'))
    formData.append('file', file)
    axios.post(urlPre + '/upload_file', formData, {
      headers: {
        'Content-Type': 'multipart/form-data;charset=UTF-8',
        'Uid': util.cookies.get('uuid')
      }
    })
  },
  upload_material_price_file (file) {
    const formData = new FormData()
    formData.append('file', file)
    return axios.post(urlPre + '/upload_material_price_file', formData, {
      headers: {
        'Content-Type': 'multipart/form-data;charset=UTF-8'
      }
    })
  },
  update_price_list (data) {
    return axios.post(urlPre + '/material_price_update', data, {

    })
  },

  download_brand_price (data) {
    return axios.post(urlPre + '/download_brand_price', data, {
    })
  },

  save_material_price_summary (data) {
    return axios.post(urlPre + '/save_material_price_summary', data, {

    })
  }
}
