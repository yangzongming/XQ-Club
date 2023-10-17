<template>
  <div class="app-container">
    <div style="margin-bottom: 30px;"></div>
    <el-upload
      :on-change="upload_File"
    >
      <el-button size="small" type="primary">导入</el-button>
    </el-upload>
    <!--列表-->
    <div style="margin-bottom: 30px;"></div>
  </div>
</template>
<script>
  import upload from '@/api/upload'
  export default{
    methods:{
      upload_File(file, filelist) {
        upload.uploadFile(file.raw)
      }
    }
  }
</script>
