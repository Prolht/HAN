<template>
<div class="container">
  <el-card class="box-card">
      <div class="title">{{title}}</div>
      <div v-for="(sentence, id) in poem"
        :key="id" class="poem">
          {{sentence}}
      </div>
  </el-card>
  <div class="btn">
   <el-button icon="el-icon-more" round
  @click="SingleCharacterPage()">探索</el-button>
    <!-- <el-button>Enter</el-button> -->
  </div>
   <!-- <el-col :span="6">
    <el-card shadow="always">
      <div class="title">{{title}}</div>
      <div v-for="(sentence, id) in poem"
        :key="id" class="poem">
          {{sentence}}
      </div>
    </el-card>
  </el-col> -->
</div>
</template>

<script>
import {apigetPoem} from '@/service/apiV2'

export default {
  name: 'IndexPage',
  data () {
    return {
      title: '',
      poem: ''
    }
  },
  methods: {
    // 获取每日一诗
    getDailyPoem () {
      apigetPoem().then((res) => {
        this.title = res.data.title
        this.poem = res.data.content
        // api 接口的结果
      }).catch((err) => {
        console.log(err && err.response)
      })
    },
    SingleCharacterPage () {
      this.$router.push({
        name: 'SinglePage',
      })
    }, // 进入页面
  },
  // created: function () {
  //   this.pageSize = 5
  //   this.currentPage = 1
  //   this.getTasksList()
  // },
  mounted: function () {
    this.getDailyPoem()
  }
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

  .container {
    padding: 100px;
  }
  .title{
    text-align: center;
    font-size: 45px;
    font:bolder;
    margin:7px;
  }
  .poem{
    text-align: center;
    font-size: 25px;
    margin: 2px;
  }

  .box-card {
    width: 500px;
    font-family: "微软雅黑";
    border-radius: 6px;
    position: relative;
    padding: 70px;
    margin-left:auto;
    margin-right: auto;
    background-color: transparent;
    /* opacity: 0.7; */
  }
  .btn{
    padding: 15px;
    text-align: right;
    font: bold;
  }

</style>
