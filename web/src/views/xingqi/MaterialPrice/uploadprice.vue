<template>
  <div class="app-container">
    <div>
      <div style="margin-bottom: 30px;"></div>
      <span>这个功能是为了收集星奇采购部零散的询价单</span>
      <el-divider></el-divider>
      <el-upload :on-change="upload_File">
        <el-button size="small" type="primary" :style="{ display: uploadButtonVisible }">上传报价单</el-button>
      </el-upload>
      <div style="margin-bottom: 15px;"></div>
    <div>
    <el-table
      :data="itemList"
      style="width: 100%"
      max-height="400"
      ref="scrollTable"
      border fit highlight-current-row>
      <el-table-column
        prop="brand"
        label="品牌"
        width="180">
      </el-table-column>
      <el-table-column
        prop="mode"
        label="类型"
        width="180">
      </el-table-column>
      <el-table-column
        prop="name"
        label="产品名称">
      </el-table-column>
      <el-table-column
        prop="number"
        label="规格型号">
      </el-table-column>
      <el-table-column
        prop="price"
        label="单价（含税）">
      </el-table-column>
    </el-table>
    <el-button size="small" type="primary" @click="submit()" :style="{ display: submitButtonVisible }">提交</el-button>
    <div style="margin-bottom: 30px;"></div>

    <add-price-summary :dialogVisible="addPriceSummaryDialogVisible" @dialogClosed="addPriceSummaryDialogClosed"></add-price-summary>
  </div>
</template>

<script>
  import upload from '@/api/upload'
  import addPriceSummary from './add_price_summary'
  export default{
    components:{
      addPriceSummary,
    },

    data(){
      return{
        itemList:[],
        submitButtonVisible: 'none',
        uploadButtonVisible: '',
        addPriceSummaryDialogVisible: false,
      }
    },

    methods:{
      upload_File(file, filelist) {
        upload.upload_material_price_file(file.raw).then(res=>{
           this.itemList = res.data;
           console.log(this.itemList)
           this.submitButtonVisible = ''
           this.uploadButtonVisible = 'none'
        })
      },
      submit(){
        this.addPriceSummaryDialogVisible = true
        console.log('submit clock')
        upload.update_price_list(this.itemList).then(res=>{
          console.log(res)
        })
      },
      addPriceSummaryDialogClosed(){
        this.addPriceSummaryDialogVisible = false;
      },
    }
  }
</script>
