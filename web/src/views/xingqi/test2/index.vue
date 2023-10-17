<template>
  <div class="app-container">
    <div style="margin-bottom: 30px;"></div>
    <el-button type="primary" icon="el-icon-plus" size="mini" @click="createArticle" ></el-button>
    <div style="margin-bottom: 10px;"></div>

    <el-upload
            ref="upload"
            action=""
            accept=".xlsx,.xls"
            :on-change="upload_File"
          <el-button size="small" type="primary">导入</el-button>
    </el-upload>
    <!--列表-->
    <!---
    <el-table style="width: 100%"
              :data="configList"
              v-loading.body="tableLoading"
              element-loading-text="加载中"
              border fit highlight-current-row>
      <el-table-column prop="onlineConfigId" label="ID"></el-table-column>
      <el-table-column prop="projectName" label="所属项目"></el-table-column>
      <el-table-column prop="name" label="参数名"></el-table-column>
      <el-table-column prop="content" label="参数值"></el-table-column>
      <el-table-column prop="summary" label="描述"></el-table-column>
      <el-table-column prop="createTime" label="创建时间"></el-table-column>
      <el-table-column prop="modifyTime" label="修改时间"></el-table-column>
      <el-table-column width="180px" label="操作">
        <template slot-scope="scope">
          <el-tooltip content="修改" placement="top">
            <el-button type="primary" icon="el-icon-edit" circle @click="editConfig(scope.$index,scope.row)"></el-button>
          </el-tooltip>
          <el-tooltip content="删除" placement="top">
            <el-button type="primary" icon="el-icon-delete" circle @click="deleteConfig(scope.$index,scope.row)"></el-button>
          </el-tooltip>
        </template>
      </el-table-column>
    </el-table>
    --->

    <div style="margin-bottom: 30px;"></div>
    <!--分页-->
    <el-pagination
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
      :current-page="tablePage.current"
      :page-sizes="[10, 20, 30, 40, 50]"
      :page-size="tablePage.count"
      layout="total, sizes, prev, pager, next, jumper"
      :total="tablePage.total">
    </el-pagination>

    <add-config :dialogVisible="addArtilceDialogVisible" @dialogClosed="addArticleDialogClosed" :onlineConfigId="currentSelectArticleId"></add-config>

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
        tablePage: {
          current: 1,
          pages: null,
          count: 10,
          total: null
        },
        tableQuery: {
          name: null,
          productTypeId: null,
        },
        configList:[],
        addArtilceDialogVisible:false,
        currentSelectArticleId:0,
      }
    },
    created() {
      this.initData()
      this.loadDataFromServer()
    },
    methods:{
      initData(){

      },
      loadDataFromServer(current){

      },

      upload_File(file, filelist) {
         upload.uploadFile(file.raw)
      },

      //分页
      handleSizeChange(val) {
        this.tablePage.count = val;
        this.loadDataFromServer();
      },
      handleCurrentChange(val) {
        this.tablePage.current = val;
        this.loadDataFromServer();
      },
      //创建
      createArticle(){
        this.article = {};
        this.currentSelectArticleId = 0;
        this.addArtilceDialogVisible = true;
      },
      //修改
      editConfig(idx , row){
        this.currentSelectArticleId = row.onlineConfigId;
        this.addArtilceDialogVisible = true;
      },
      //删除
      deleteConfig(idx, row){
        this.$alert('确定要删除该参数吗？', '提示', {
          confirmButtonText: '确定',
          callback: action => {
            onlineConfigApi.deleteConfig(row.onlineConfigId).then(
              res=>{
                this.loadDataFromServer();
              }
            )
          }
        });
      },

      addArticleDialogClosed(){
        this.addArtilceDialogVisible = false;
      },

      //查看
      joindBookClick(idx,row){
        this.$router.push({ name: 'articlebooks', params: { articleId: row.id ,articleTitle:row.title }})
      },
    }
  }
</script>
