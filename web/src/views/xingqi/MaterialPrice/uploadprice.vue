<template>
    <div>
      <div style="margin-bottom: 30px;"></div>
      <span>这个功能是为了收集星奇采购部零散的询价单</span>
      <el-divider></el-divider>

      <el-upload :on-change="upload_File">
        <el-button size="small" type="primary">上传询价单</el-button>
      </el-upload>
    <div>
    <el-table
      :data="tableData"
      style="width: 100%">
      <el-table-column
        prop="date"
        label="日期"
        width="180">
      </el-table-column>
      <el-table-column
        prop="name"
        label="姓名"
        width="180">
      </el-table-column>
      <el-table-column
        prop="address"
        label="地址">
      </el-table-column>
    </el-table>
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
