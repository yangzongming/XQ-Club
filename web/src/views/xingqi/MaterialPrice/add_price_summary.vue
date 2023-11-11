<template>
  <el-dialog :visible.sync="curDialogVisible" width="70%" :before-close="handleClose">
    <h3 style="padding-left: 10px">添加报价单</h3>
    <el-form ref="form" :model="config" label-width="80px">

      <el-form-item label="备注信息" style="width: 50%">
        <el-input type="textarea" :rows="5" placeholder="请输入此次报价需要备注的信息" v-model="config.info"></el-input>
      </el-form-item>
      <el-form-item label="供应商" style="width: 50%">
        <el-input type="textarea" :rows="1" placeholder="请输入此次报价的公司名称" v-model="config.supplier"></el-input>
      </el-form-item>
      <el-form-item align="center">
        <el-button type="primary" @click="onSubmit" align="center" style="width: 96%">提交报价</el-button>
      </el-form-item>

    </el-form>
  </el-dialog>
</template>

<script>

  import {parseTime, resetTemp} from '@/utils'
  import upload from '@/api/upload'
  export default {

    components: {

    },

    props:["dialogVisible","priceList","fileMd5","fileName"],

    name: 'addPriceSummary',

    watch:{
      dialogVisible(val){
        this.curDialogVisible = val;
      },
      priceList(val){
        this.curPriceList = val;
      },
      fileMd5(val){
        this.curFileMd5 = val;
      },
      fileName(val){
        this.curFileName = val;
      },
    },

    created(){
      console.log('dialog created')
      this.initData();
    },

    data() {
      return {
        config: {
          info:'',
          supplier: '',
        },
        curDialogVisible:this.dialogVisible,
        curPriceList: this.priceList,
        curFileMd5: this.fileMd5,
        curFileName: this.fileName,
       }
    },
    methods: {
      initData(){

      },
      handleClose(){
        this.$emit('dialogClosed',true);
      },
      onSubmit(){
        if(this.config.info == '' || this.config.info == null){
          this.$alert('请输入备注信息')
          return false;
        }
        if(this.config.supplier == '' || this.config.supplier == null){
          this.$alert('请输入供应商信息')
          return false;
        }
        upload.save_material_price_summary({
          'list': this.curPriceList,
          'info': this.config.info,
          'supplier': this.config.supplier,
          'file_md5': this.curFileMd5,
          'filename': this.curFileName,
        }).then(res=>{
          console.log(res)
          if(res.data.code == 0){
            this.$emit('dialogClosed',true);
            this.$alert('报价上传成功～')
          }else{
            this.$alert(res.data.errmsg)
            this.$emit('dialogClosed',true);
          }
        })
      }
    }
  }
</script>
