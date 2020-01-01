<template>
  <el-button
    :size="size"
    type="primary"
    @click="handleSubmit"
    :loading="isLoading > 0">
    全部提交
  </el-button>
</template>

<script>
import {labelSubmitMixin} from './labelSubmitMixin'

export default {
  name: 'LabelSubmitAllBtn',
  props: ['isDirtyList', 'sentences', 'userId', 'itemSuccess', 'size'],
  mixins: [labelSubmitMixin],
  data () {
    return {
      isLoading: 0
    }
  },
  methods: {
    handleSubmit () {
      if (this.isLoading) return
      this.submitAllSentences()
    },
    btnStartLoading () {
      this.isLoading++
    },
    btnEndLoading () {
      this.isLoading--
      if (this.isLoading === 0) {
        this.$notify({
          title: '提交成功',
          message: '全部提交成功',
          type: 'success'
        })
      }
    },
    submitAllSentences () {
      this.success = this.itemSuccess
      this.isDirtyList.forEach((item, ind) => {
        if (item) {
          this.btnStartLoading()
          this.submitSentence(this.sentences[ind], ind)
        }
      })
    },
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
