<template>
  <div class="app-container">
    <div>
      <div style="margin-bottom: 30px;"></div>
      <span>这个功能是为了收集星奇采购部零散的询价单</span>
      <el-divider></el-divider>
      <el-upload
      :on-change="upload_File"
      :auto-upload="false"
      >
        <el-button size="small" type="primary" :style="{ display: uploadButtonVisible }">上传报价单</el-button>
      </el-upload>
      <div style="margin-bottom: 15px;"></div>
    <div>

    <el-select v-model="brand_value" multiple placeholder="请选择品牌">
      <el-option
        v-for="item in brandOptions"
        :key="item.value"
        :label="item.value"
        :value="item.value">
      </el-option>
    </el-select>

    <el-select v-model="mode_value" multiple placeholder="请选择类型">
      <el-option
        v-for="item in modeOptions"
        :key="item.value"
        :label="item.value"
        :value="item.value">
      </el-option>
    </el-select>

    <el-button size="small" type="primary" @click="downloadBrandPrice()">下载</el-button>


    <div style="margin-bottom: 15px;"></div>

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

    <add-price-summary
    :dialogVisible = "addPriceSummaryDialogVisible"
    :priceList = "itemList"
    :fileMd5 = "file_md5"
    :fileName = "filename"
    @dialogClosed="addPriceSummaryDialogClosed"></add-price-summary>
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
        brandOptions:[
          {'value': 'Fujikin'},
          {'value': 'Tk-fujikin'},
          {'value': 'Swagelok'},
          {'value': 'Fitok'},
          {'value': 'Unilok'},
          {'value': 'Dk-lok'},
          {'value': 'Super-lok'},
          {'value': 'Horiba'},
          {'value': 'Brooks'},
          {'value': 'Tem-tech'},
          {'value': 'CKD'},
          {'value': 'Festo'},
          {'value': 'Parker'},
          {'value': 'SMC'},
          {'value': 'Omron'},
          {'value': '星奇'},
          {'value': '皓固'},
          {'value': 'Azibil'},
          {'value': '科百特'},
          {'value': '方顿'},
          {'value': '创源'},
          {'value': '洁安'},
          {'value': 'Pall'},
          {'value': 'Entegris'},
          {'value': 'IFM'},
          {'value': 'Wika'},
          {'value': 'UE'},
          {'value': 'Pureron'},
          {'value': 'Nagano'},
          {'value': 'Hamlet'},
          {'value': 'Truck'},
          {'value': 'Eazjoin'},
          {'value': '聚创'},
          {'value': '阀乐'}
        ],
        modeOptions:[
          {'value': '球阀'},
          {'value': 'VCR-隔膜阀'},
          {'value': 'VCR-减压阀'},
          {'value': 'VCR-单向阀'},
          {'value': '接头'},
          {'value': 'MFC'},
          {'value': '过滤器'},
          {'value': 'Gasket'},
          {'value': 'igs-block'},
          {'value': 'igs-隔膜阀'},
          {'value': '波纹管阀'},
          {'value': 'PT'},
          {'value': '未知'}
        ],

        brand_value: '',
        mode_value: '',

        itemList:[],
        file_md5:'',
        filename:'',
        submitButtonVisible: 'none',
        uploadButtonVisible: '',
        addPriceSummaryDialogVisible: false,
      }
    },

    methods:{
      upload_File(file, filelist) {
        upload.upload_material_price_file(file.raw).then(res=>{
           if(res.data.code == 0){
             this.itemList = res.data.material_list;
             this.file_md5 = res.data.file_md5;
             this.filename = res.data.filename;
             //console.log(this.itemList)
             this.submitButtonVisible = ''
             this.uploadButtonVisible = 'none'
           }else{
             this.$alert(res.data.errmsg)
           }
        })
      },
      submit(){
        this.addPriceSummaryDialogVisible = true
      },
      addPriceSummaryDialogClosed(){
        this.addPriceSummaryDialogVisible = false;
      },

      //下载系统中根据 品牌和类型的报价
      downloadBrandPrice(){
        let data = {
          'brand': this.brand_value,
          'mode': this.mode_value,
        }
        console.log('fuck')
        upload.download_brand_price(data).then(res=>{
        })
      },
    }
  }
</script>
