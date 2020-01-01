<template>
<div class="search-page">
    <base-header></base-header>
    <el-main class="main-container" v-loading="loading">
      <div class="">
        <el-input
          :size="isMobile ? 'mini' : ''"
          class="search-input"
          :value="searchInp"
          @keyup.enter.native="handleSearch"
          placeholder="搜索">
        </el-input>
      </div>
      <div class="characters-list">
        <div
          class="characters"
          v-for="(sentence, sentenceInd) in sentences"
          :key="sentence.id"
          @mouseup="endSelect()">
          <div class="">
            <span class="sentence-index">{{ (currentPage - 1) * pageSize + sentenceInd + 1 }}.</span>
            <label-submit-btn
              :is-dirty="isDirtyList[sentenceInd]"
              :user-id="userId"
              :sentence="sentence"
              :success="() => sentenceClean(sentenceInd)">
            </label-submit-btn>
            <el-button
              size="mini"
              :style="{background: `rgb(255, 255, ${(10-sentence.results.length)/10*255})`}"
              @click="showOthersWork(sentenceInd)">
              {{sentence.results.length}}
            </el-button>
          </div>
          <div class="others-work" v-show="isShowOthersList[sentenceInd]">
            <div v-for="(otherSentence, ind) in sentence.results" :key="ind">
              <span class="others-username">{{otherSentence.username}}</span>
              <span class="word" v-for="(word, ind) in otherSentence.result" :key="ind">{{ word | displaySpace }}</span>
            </div>
          </div>
          <div>
            <span
              class="word"
              v-for="(word, wordInd) in sentence.result"
              :key="wordInd"
              :class="{'word-selected': isWordSelected(sentenceInd, wordInd)}"
              @dblclick="!isMobile && separateWord(sentenceInd, wordInd, word)"
              @mousedown="!isMobile && startSelect(sentenceInd, wordInd)"
              @mouseup.stop="!isMobile && endSelect(sentenceInd, wordInd)"
              @mousemove="!isMobile && selectingWord(sentenceInd, wordInd)"
              @touchstart="isMobile && mobileTouchWord(sentenceInd, wordInd, word)"
              @touchmove="isMobile && mobileTouchmove()"
              @touchend="isMobile && mobileTouchend()">
              {{ word | displaySpace }}
            </span>
          </div>
        </div>
      </div>
      <div class="block">
        <el-pagination
          class="pagination"
          :small="Boolean(isMobile)"
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="currentPage"
          :page-sizes="[1, 5, 10, 20, 30, 50, 100]"
          :page-size="pageSize"
          :layout="isMobile ? 'prev, pager, next' : 'sizes, prev, pager, next, jumper'"
          :total="totalItems">
        </el-pagination>
      </div>
    </el-main>
  </div>
</template>

<script>
import { apiSearch } from '@/service/apiV2'
import BaseHeader from '@/components/BaseHeader'

export default {
  name: 'SearchPage',
  components: {
    BaseHeader,
  },
  data () {
    return {
      simplified: '',
      traditional: '',
      allusion: '',
      pinyin: '',
      img_file: '',
    }
  },
  computed: {
  },
  methods: {
    getTasksList () {
      apiSearch().then((res) => {
        this.simplified = res.data.simplified
        this.traditional = res.data.traditional
        this.allusion = res.data.allusion
        this.pinyin = res.data.pinyin
        this.img_file = res.data.img_file
      }).catch((err) => {
        console.log(err && err.response)
        try {
          this.$notify.error({
            title: '出错了',
            message: err.response.statusText,
          })
        } catch (e) {
          this.$notify.error({
            title: '出错了',
            message: '出错了',
          })
        }
      })
    },
    goLabelPage (projectId) {
      this.$router.push({
        name: 'LabelPage',
        params: { projectId: projectId },
        query: { page: 1, size: 30 },
      })
    },
    goCecLabelPage (projectId) {
      this.$router.push({
        name: 'CecLabelPage',
        params: { projectId: projectId },
        query: { page: 1, size: 30 },
      })
    },
    goSinglePage (character) {
      this.$router.push({
        name: 'SinglePage',
        params: { character: character },
      })
    },
    alertMessage () {
      alert('暂不支持')
    }
  },
  mounted () {
    this.getTasksList()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.card-container {
  width: calc(100% - 30px);
  max-width: 1200px;
  margin: 20px auto 0;
}
.project {
  margin: 10px 0;
  padding: 10px;
  color: #fff;
  cursor: pointer;
}
.box-card {
  margin: 10px 0;
  min-height: 200px;
  background-color: #8cc5ff;
  color: #fff;
}
.task-item {
  padding: 5px 20px;
  cursor: pointer;
}
.task-item:hover {
  background-color: #cad5e2;
  color: #66b1ff;
}
</style>
