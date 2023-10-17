<template>
  <div class="app-container">
    <div style="margin-bottom: 30px;"></div>
    <el-upload
            ref="upload"
            action=""
            accept=".xlsx,.xls"
            :on-change="upload_File"
          <el-button size="small" type="primary">导入</el-button>
    </el-upload>
    <!--列表-->
    <div style="margin-bottom: 30px;"></div>
  </div>
</template>


<script>
  import upload from '@/api/upload'
  import addConfig from './add_config'
  import {root,confirm,pageParamNames} from '@/utils/constants'
  import {parseTime, resetTemp} from '@/utils'

  export default{

    components:{
      addConfig
    },

    data(){
      return{
        tableLoading: false,
        parseTime: parseTime,
      }
    },
    created() {

    },
    methods:{
      upload_File(file, filelist) {
         upload.uploadFile(file.raw)
      },
    }
  }
</script>
