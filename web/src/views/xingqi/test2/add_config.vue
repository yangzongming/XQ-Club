<template>
  <el-dialog :visible.sync="curDialogVisible" width="70%" :before-close="handleClose">
    <h3 style="padding-left: 10px" v-if="isInsert">添加在线参数</h3>
    <h3 style="padding-left: 10px" v-if="!isInsert">修改参数</h3>
    <el-form ref="form" :model="config" label-width="80px">

      <el-form-item label="参数名" style="width: 50%">
        <el-input v-model="config.name" placeholder="请输入标题20个字以内"></el-input>
      </el-form-item>

      <el-form-item label="参数值" style="width: 50%">
        <el-input type="textarea" :rows="6" placeholder="请输入值" v-model="config.content"></el-input>
      </el-form-item>

      <el-form-item label="描述" style="width: 50%">
        <el-input type="textarea" :rows="1" placeholder="请输入描述" v-model="config.summary"></el-input>
      </el-form-item>

      <el-form-item label="项目" style="width: 50%">
        <template>
          <el-select v-model="config.projectName" placeholder="请选择项目">
            <el-option
              v-for="city in projects"
              :key="city.value"
              :label="city.name"
              :value="city.value">
            </el-option>
          </el-select>
        </template>
      </el-form-item>
      <el-form-item align="center">
        <el-button type="primary" v-if="isInsert" @click="onSubmit" align="center" style="width: 96%">立即创建</el-button>
        <el-button type="primary" v-if="!isInsert" @click="onSubmit" align="center" style="width: 96%">保存</el-button>
      </el-form-item>
    </el-form>
  </el-dialog>
</template>

<script>

  //import onlineConfigApi from '@/api/onlineConfig';
  import {parseTime, resetTemp} from '@/utils'

  export default {

    components: {

    },

    props:["dialogVisible","onlineConfigId"],

    name: 'addConfig',

    watch:{
      onlineConfigId(val){
        if(val > 0){
          this.curConfigId = val;
          this.loadConfigDataFromServer(this.curConfigId);
        }else{
          this.isInsert = true;
          this.config = {};
        }
      },
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
        isInsert:true,
        curConfigId:this.configId,
        curDialogVisible:this.dialogVisible,
        currentDate:'',
        projects:[
          {"name":"地瓜英语-四级","value":"potatos_cet4"},
          {"name":"地瓜英语-六级","value":"potatos_cet6"},
          {"name":"微信小程序","value":"wechat_dish"}
          ],
      }
    },
    methods: {
      initData(){
        //初始化数据
        if(this.curConfigId != null && this.curConfigId > 0){
          //加载数据
          loadConfigDataFromServer(this.curConfigId);
          this.currentDate = new Date();
        }
      },
      onSubmit() {

      },

      loadConfigDataFromServer(curConfigId){

      },
      handleClose(){
        this.$emit('dialogClosed',true);
      },
    }
  }
</script>

<style scoped>

</style>
