<template>
  <div class="container">
    <div>
      <el-input size="small" placeholder="搜索"
      v-model="input" clearable
      style="margin-right:30px;position:relative;float:right;width:150px;">
      <el-button @click="getCharacter()" slot="append" icon="el-icon-search"></el-button>
      </el-input>
    </div>
    <el-card class="box-card">
      <div class="main-character">
          <!-- <span class="demonstration">{{ fit }}</span> -->
          <el-button type="info" icon="el-icon-message" size="mini" circle></el-button>
            <span style="font-size:15px">简体中文</span>
            <el-container height="80px">
              <el-aside width="70px" class="character">{{simplified}}</el-aside>
              <el-main style="padding:0px;">
                <div class="block1">
                  <div class="pinyin" style="width:80px; margin:0px">
                    <el-divider direction="vertical" style="color:black;"></el-divider>
                    <span>{{pinyin}}</span>
                  </div>
                  <div class="traditional" style="font-size:40px;width:80px;margin:0px;">
                    <el-divider direction="vertical" style="color:black;"></el-divider>
                    <span>{{traditional}}</span>
                  </div>
                </div>
                <div class="block2">
                  <el-image class="image" :src="img_url" style="right:0px"></el-image>
                </div>
              </el-main>
            </el-container>
            <el-divider></el-divider>
      </div>
      <div class="main-character">
        <el-button type="info" icon="el-icon-message" size="mini" circle></el-button>
            <span style="font-size:15px">典故</span>
        <div>{{allusion}}</div>
      </div>
    </el-card>
  </div>
</template>

<script>
import {apipostCharacter} from '@/service/apiV2'
// import BaseHeader from '@/components/BaseHeader'
export default {
  name: 'SinglePage',
  data () {
    return {
      character: '声', // 搜索时传的参数
      simplified: '',
      traditional: '',
      allusion: '',
      pinyin: '',
      img_file: '',
      isMobile: false,
      img_url: '',
      input: '',
    }
  },
  methods: {
    // 获取文字列表
    getCharacter () {
      this.loading = true
      if (this.input) {
        this.character = this.input
      }
      apipostCharacter(this.character).then((res) => {
        this.loading = false
        this.img_file = res.data.img_file
        this.simplified = res.data.simplified
        this.traditional = res.data.traditional
        this.allusion = res.data.allusion
        this.pinyin = res.data.pinyin.split(',')[0]
        // this.img_file  /media/cha/%E5%A3%B0.jpg
        this.img_url = '../../..' + this.img_file
      }).catch((err) => {
        console.log(err && err.response)
      })
    },
  },
  mounted: function () {
    this.character = '声'
    this.getCharacter()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
 .container {
    padding: 100px;
  }
  .box-card {
      width: 600px;
      height: 400px;
      font-family: KaiTi;
      border-radius: 6px;
      position: relative;
      margin-left:auto;
      margin-right: auto;
      background-color: transparent;
      /* opacity: 0.7; */
    }
    .main-character {
      height: 150px;
      margin-top: 0%;
      position: relative;
    }
    .character {
      font:bolder;
      font-size: 70px;
    }
    .image{
      position:absolute;
      right:0px;
      width: 70px;
      height: 70px
    }
    .block1{
      float: left;
      height: 80px;
    }
    .block1{
      float: left;
    }
</style>
