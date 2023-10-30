<template>
  <el-dialog :visible.sync="curDialogVisible" width="70%" :before-close="handleClose">
    <h3 style="padding-left: 10px">添加报价单</h3>
    <el-form ref="form" :model="config" label-width="80px">
      <el-form-item label="报价备注" style="width: 50%">
        <el-input type="textarea" :rows="1" placeholder="请输入此次报价需要备注的信息" v-model="config.summary"></el-input>
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

    props:["dialogVisible","priceList"],

    name: 'addPriceSummary',

    watch:{
      dialogVisible(val){
        this.curDialogVisible = val;
      },
      priceList(val){
        this.curPriceList = val;
      },
    },

    created(){
      console.log('dialog created')
      this.initData();
    },

    data() {
      return {
        config: {
          onlineConfigId: 0,
          name: '',
          content:'',
          projectName: '',
        },
        curDialogVisible:this.dialogVisible,
        curPriceList: this.priceList,
       }
    },
    methods: {
      initData(){

      },
      handleClose(){
        this.$emit('dialogClosed',true);
      },
      onSubmit(){
        upload.save_material_price_summary({
          'list': this.curPriceList,
          'info': this.config.summary,
        }).then(res=>{
          console.log(res)
        })
      }
    }
  }
</script>
