<template>
  <el-button
    class="submit-btn btn"
    circle
    :loading="isLoading"
    :icon="isDirty ? 'el-icon-edit' : sentence.labeled ? 'el-icon-check' : 'el-icon-edit-outline'"
    :type="isDirty ? 'warning' : sentence.labeled ? 'success' : ''"
    @click="handleSubmit"
  ></el-button>
</template>

<script>
import {labelSubmitMixin} from './labelSubmitMixin'

export default {
  name: 'LabelSubmitBtn',
  props: ['isDirty', 'sentence', 'userId', 'success'],
  mixins: [labelSubmitMixin],
  data () {
    return {
      isLoading: false
    }
  },
  methods: {
    handleSubmit () {
      if (this.isLoading) return
      this.btnStartLoading()
      this.submitSentence(this.sentence)
    },
    btnStartLoading () {
      this.isLoading = true
    },
    btnEndLoading () {
      this.isLoading = false
    },
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .submit-btn.btn {
    width: 33px;
    height: 33px;
    padding: 0;
    font-size: 15px;
  }
</style>
