<template>
  <el-dialog :visible.sync="curDialogVisible" width="70%" :before-close="handleClose">
    <h3 style="padding-left: 10px">添加报价单</h3>
    <el-form ref="form" :model="config" label-width="80px">
      <el-form-item label="参数名" style="width: 50%">
        <el-input v-model="config.name" placeholder="请输入summary"></el-input>
      </el-form-item>
      <el-form-item label="参数值" style="width: 50%">
        <el-input type="textarea" :rows="6" placeholder="请输入值" v-model="config.content"></el-input>
      </el-form-item>
      <el-form-item label="描述" style="width: 50%">
        <el-input type="textarea" :rows="1" placeholder="请输入描述" v-model="config.summary"></el-input>
      </el-form-item>
      <el-form-item align="center">
        <el-button type="primary" @click="onSubmit" align="center" style="width: 96%">立即创建</el-button>
      </el-form-item>

    </el-form>
  </el-dialog>
</template>

<script>

  import {parseTime, resetTemp} from '@/utils'

  export default {

    components: {

    },

    props:["dialogVisible"],

    name: 'addPriceSummary',

    watch:{
      dialogVisible(val){
        this.curDialogVisible = val;
      },
    },

    created(){
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
    },
    methods: {
      initData(){

      }
    }
  }
</script>
