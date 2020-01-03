<template>
  <div class="">
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
      <el-form-item label="简体中文" prop="name">
        <el-input v-model="ruleForm.simplified"></el-input>
      </el-form-item>
      <el-form-item label="繁体中文" prop="region">
        <el-input v-model="ruleForm.traditional"></el-input>
      </el-form-item>
      <el-form-item label="请输入典故" required>
        <el-input
          type="textarea"
          :rows="2"
          v-model="ruleForm.allusion">
        </el-input>
      </el-form-item>
      <el-upload
        class="upload-demo"
        action="apiUpload"
        :on-preview="handlePreview"
        :on-remove="handleRemove"
        :file-list="fileList"
        list-type="picture">
        <el-button size="small" type="primary">点击上传</el-button>
        <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
      </el-upload>
      <el-form-item label="密码" prop="pass">
        <el-input type="password" v-model="ruleForm.pass" autocomplete="off"></el-input>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>

// import {apiUpload} from '@/service/apiV2'
// import BaseHeader from '@/components/BaseHeader'
export default {
  data () {
    return {
      img: {name: 'hanzi.jpeg', url: 'https://d/?imageMogr2/thumbnail/360x360/format/webp/quality/100'},
      ruleForm: {
        simplified: '',
        traditional: '',
        allusion: '',
        pinyin: '',
        img_file: false,
        type: [],
        resource: '',
        desc: ''
      },
      rules: {
        simplified: [
          { required: true, message: '请输入简体中文', trigger: 'blur' },
          { min: 1, max: 1, message: '长度为1个字符', trigger: 'blur' }
        ],
        traditional: [
          { required: false, message: '请输入繁体中文', trigger: 'blur' },
          { min: 1, max: 1, message: '长度为1个字符', trigger: 'blur' }
        ],
        allusion: [
          { required: false, message: '请输入典故', trigger: 'blur' },
        ],
        pinyin: [
          { type: 'date', required: true, message: '请选择时间', trigger: 'change' }
        ],
        img_file: [
          { type: 'array', required: true, message: '请至少选择一个活动性质', trigger: 'change' }
        ],
        resource: [
          { required: true, message: '请选择活动资源', trigger: 'change' }
        ],
        desc: [
          { required: true, message: '请填写活动形式', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    handleRemove (file, fileList) {
      console.log(file, fileList)
    },
    handlePreview (file) {
      console.log(file)
    },
    submitForm (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          alert('submit!')
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .other {
    height: 150px;
  }
  .main-container {
    width: 100%;
    max-width: 1200px;
    margin: 1px auto 0;
  }
  .table-text-blue{
  color: rgb(3, 3, 5);
  cursor:pointer;
  }
  .table-text-gray{
    color: #9132eb;
  }
  .el-table th.is-leaf{
    background: #9132eb;
    border-bottom: none;
  }
  .el-table--border th{
    border-color:#FFF;
    font-weight: normal;
  }
  .el-table--border{
    border:none;
  }
  .el-table,.el-table thead{
    color:rgb(5, 3, 7);
  }
  .el-table--border::after, .el-table--group::after{
    background-color: #fff;
  }
  .el-table th, .el-table tr {
    background-color: transparent;
    }
</style>
