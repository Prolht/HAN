<template>
  <div class="label-page">
    <base-header></base-header>
    <el-main class="main-container" v-loading="loading">
      <div class="">
        <label-submit-all-btn
          :size="isMobile ? 'mini' : ''"
          :is-dirty-list="isDirtyList"
          :user-id="userId"
          :sentences="sentences"
          :itemSuccess="(sentenceInd) => sentenceClean(sentenceInd)">
        </label-submit-all-btn>
        <el-input
          :size="isMobile ? 'mini' : ''"
          class="search-input"
          :value="searchInp"
          @keyup.enter.native="handleSearch"
          placeholder="搜索">
        </el-input>
        <el-input
          :size="isMobile ? 'mini' : ''"
          class="index-input"
          v-model="indexInp"
          @keyup.enter.native="handleIndexJump"
          placeholder="序号">
        </el-input>
      </div>
      <div class="sentence-list">
        <div
          class="sentence"
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
import BaseHeader from '@/components/BaseHeader'
import LabelSubmitBtn from './children/LabelSubmitBtn'
import LabelSubmitAllBtn from './children/LabelSubmitAllBtn'
import {apiGetItemsList} from '@/service/getData'

// 句子是否编辑监控
var sentenceDirty = {
  data () {
    return {
      isDirtyList: [],
    }
  },
  computed: {

  },
  methods: {
    sentenceDirty (sentenceInd) {
      this.$set(this.isDirtyList, sentenceInd, true)
    },
    sentenceClean (sentenceInd) {
      this.$set(this.isDirtyList, sentenceInd, false)
    },
    sentenceCleanAll () {
      this.isDirtyList = []
    },
    isSentenceDirty () {
      return this.isDirtyList.indexOf(true) > -1
    },
  }
}

export default {
  name: 'LabelPage',
  mixins: [sentenceDirty],
  components: {
    BaseHeader,
    LabelSubmitBtn,
    LabelSubmitAllBtn,
  },
  data () {
    return {
      userId: parseInt(localStorage.getItem('userId')),
      projectId: parseInt(this.$route.params.projectId),
      sentences: [],

      isSelecting: false,
      wordFrom: {},
      wordEnd: {},

      currentPage: parseInt(this.$route.query.page),
      pageSize: parseInt(this.$route.query.size),
      totalItems: this.currentPage * this.pageSize,

      searchInp: '',
      indexInp: '',

      isShowOthersList: [],

      loading: true,

      isMobile: false,
      longPressTimer: 0,
    }
  },
  filters: {
    displaySpace (value) {
      return value.replace(/\s/g, '　') // 换成全角空格
    }
  },
  computed: {

  },
  methods: {
    /**
     * 分词操作相关
     */
    separateWord (sentenceInd, wordInd, word) {
      if (word.length > 1) {
        this.sentences[sentenceInd].result.splice(wordInd, 1, ...word.split(''))
        this.sentenceDirty(sentenceInd)
      }
    },
    startSelect (sentenceInd, wordInd) {
      if (this.isSelecting) return
      this.isSelecting = true
      this.wordFrom = {sentenceInd, wordInd}
      this.wordEnd = {sentenceInd, wordInd}
      // console.log('start', sentenceInd, wordInd)
    },
    endSelect (sentenceInd, wordInd) {
      this.isSelecting = false
      // console.log('end', this.wordFrom.sentenceInd, this.wordEnd.wordInd)
      if (this.wordFrom.sentenceInd === undefined) return
      if (sentenceInd === this.wordFrom.sentenceInd) this.wordEnd = {sentenceInd, wordInd}
      this.mergeWord()
      this.wordFrom = {}
      this.wordEnd = {}
    },
    selectingWord (sentenceInd, wordInd) {
      if (!this.isSelecting) return
      if (this.wordFrom.sentenceInd === sentenceInd) this.wordEnd = {sentenceInd, wordInd}
      // console.log('move', sentenceInd, wordInd)
    },
    mergeWord () {
      var {wordFrom, wordEnd} = this
      // console.log(wordFrom, wordEnd)
      var from = Math.min(wordFrom.wordInd, wordEnd.wordInd)
      var end = Math.max(wordFrom.wordInd, wordEnd.wordInd)
      this.sentences[wordFrom.sentenceInd].result.splice(from, end - from + 1, this.sentences[wordFrom.sentenceInd].result.slice(from, end + 1).join(''))
      this.sentenceDirty(wordFrom.sentenceInd)
    },
    isWordSelected (sentenceInd, wordInd) {
      // TODO 调用太多
      var {wordFrom, wordEnd} = this
      var from = Math.min(wordFrom.wordInd, wordEnd.wordInd)
      var end = Math.max(wordFrom.wordInd, wordEnd.wordInd)
      return sentenceInd === wordFrom.sentenceInd && from <= wordInd && wordInd <= end
    },
    mobileTouchWord (sentenceInd, wordInd, word) {
      if (!this.isSelecting) {
        this.longPressTimer = setTimeout(() => {
          this.isSelecting = false
          this.wordFrom = {}
          this.wordEnd = {}
          this.separateWord(sentenceInd, wordInd, word)
        }, 500)
      }
      if (!this.isSelecting) {
        this.startSelect(sentenceInd, wordInd)
      } else {
        this.endSelect(sentenceInd, wordInd)
      }
    },
    mobileTouchend () {
      clearTimeout(this.longPressTimer)
      this.longPressTimer = 0
    },
    mobileTouchmove () {
      clearTimeout(this.longPressTimer)
      this.longPressTimer = 0
      this.isSelecting = false
    },

    /**
     * 分页相关
     */
    handleSizeChange (pageSize) {
      this.pageSize = pageSize
      this.currentPage = 1
      this.$router.push({
        name: 'LabelPage',
        params: { projectId: this.projectId },
        query: { page: 1, size: this.pageSize },
      })
    },
    handleCurrentChange (currentPage) {
      this.currentPage = currentPage
      this.$router.push({
        name: 'LabelPage',
        params: { projectId: this.projectId },
        query: { page: this.currentPage, size: this.pageSize },
      })
    },

    showOthersWork (ind) {
      this.$set(this.isShowOthersList, ind, !this.isShowOthersList[ind])
    },

    handleSearch (e) {
      this.searchInp = e.target.value
      if (this.currentPage === 1) {
        this.getItemsList()
      } else {
        this.$router.push({
          name: 'LabelPage',
          params: { projectId: this.projectId },
          query: { page: 1, size: this.pageSize },
        })
      }
    },
    handleIndexJump () {
      var num = parseInt(this.indexInp)
      if (!isNaN(num) && num > 0 && num <= this.totalItems) {
        this.indexInp = num
        var jumpPage = Math.floor((num - 1) / this.pageSize) + 1
        if (jumpPage === this.currentPage) {
          this.goIndex()
        } else {
          this.handleCurrentChange(jumpPage)
        }
      } else {
        this.indexInp = ''
        this.$notify.error({
          title: '序号有误',
          message: '输入序号有误，非数字或超过上下限',
        })
      }
    },

    /**
     * 获取、更新数据相关
     */
    getItemsList (callback) {
      this.loading = true
      apiGetItemsList(this.projectId, this.currentPage, this.pageSize, this.searchInp).then((res) => {
        this.resetData()
        this.currentPage = res.data.Current_page
        this.pageSize = res.data.page_size
        this.totalItems = res.data.total_result

        res.data.data.forEach((item) => {
          item.results.forEach(item => { item.result = JSON.parse(item.result) })
          var ind = item.results.findIndex(item => item.user === this.userId)
          if (ind > -1) {
            item.result = item.results[ind].result
            item.labeled = true
            item.resultId = item.results[ind].id
          } else {
            if (/^\[[\s\S]*\]$/.test(item.default)) {
              try {
                item.result = JSON.parse(item.default)
              } catch (e) {
                item.result = [item.text]
              }
            } else {
              item.result = [item.text]
            }
          }
        })
        this.sentences = res.data.data
        this.loading = false
        callback && callback()
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
        this.loading = false
      })
    },

    /**
     * 重置数据
     */
    resetData () {
      this.sentences = []

      this.isSelecting = false

      this.sentenceCleanAll()

      this.isShowOthersList = []
    },

    /**
     * 未提交提示
     */
    unsubmittedAlert (confirm, cancel) {
      this.$confirm('有未提交修改，是否继续？', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        confirm()
      }).catch(() => {
        cancel()
      })
    },

    /**
     * 跳到编号位置
     */
    goIndex () {
      this.$nextTick(() => {
        var anchor = this.$el.querySelectorAll('.sentence-index')[(this.indexInp - 1) % this.pageSize]
        document.documentElement.scrollTop = this.toTop(anchor)
        this.indexInp = ''
      })
    },
    toTop (node) {
      var top = 0
      while (node.offsetParent) {
        top += node.offsetTop
        node = node.offsetParent
      }
      return top
    },
  },
  mounted () {
    this.getItemsList()
    this.isMobile = navigator.userAgent.match(/(phone|pad|pod|iPhone|iPod|ios|iPad|Android|Mobile|BlackBerry|IEMobile|MQQBrowser|JUC|Fennec|wOSBrowser|BrowserNG|WebOS|Symbian|Windows Phone)/i)
    this.$el.querySelector('.sentence-list').addEventListener('contextmenu', function (e) {
      e.preventDefault()
    })
  },
  beforeRouteUpdate (to, from, next) {
    this.currentPage = parseInt(to.query.page)
    this.pageSize = parseInt(to.query.size)
    this.getItemsList(() => {
      if (this.indexInp) this.goIndex()
    })
    next()
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .menu-item {
      height: 50px;
      padding: 10px 0;
      line-height: 14px;
  }
  .main-container {
    width: 100%;
    max-width: 1200px;
    margin: 20px auto 0;
  }
  .index-input {
    width: 60px;
    float: right;
    margin-right: 5px;
  }
  .search-input {
    width: 130px;
    float: right;
  }
  .sentence {
    padding: 5px 0;
    -moz-user-select: none;
    -khtml-user-select: none;
    user-select: none;
  }
  .sentence-index {
    font-size: 18px;
  }
  .others-work {
    margin: 5px 0;
    padding: 5px 0;
    background-color: #ddd;
  }
  .others-username {
    width: 70px;
    padding-left: 3px;
    font-size: 14px;
    display: inline-block;
    overflow: hidden;
  }
  .word {
    min-width: 20px;
    color: #fff;
    text-align: center;
    background-color: #0b96d1;
    margin: 1px;
    padding: 5px;
    display: inline-block;
    cursor: pointer;
    border: 1px solid transparent;
    border-radius: 2px;
  }
  .word-selected {
    border: 1px solid #EE7600;
    background-color: #0000AA;
  }
  .pagination {
    text-align: center;
  }
</style>
