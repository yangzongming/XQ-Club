<template>
  <div class="app-container">
    <div style="margin-bottom: 30px;"></div>
    <el-upload>
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
