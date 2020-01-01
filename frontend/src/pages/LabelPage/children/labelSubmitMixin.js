import {apiLabelItem, apiUpdateItem} from '@/service/getData'

export const labelSubmitMixin = {
  methods: {
    submitSentence (sentence, ind) {
      if (sentence.labeled) {
        this.updateItem(sentence).then(res => {
          this.success(ind)
        }).catch(err => {
          console.log(err)
        }).finally(() => {
          this.btnEndLoading()
        })
      } else {
        this.labelItem(sentence).then(res => {
          try {
            res.data.result = JSON.parse(res.data.result)
          } catch (e) {
            this.$notify.error({
              title: '出错了',
              message: res.data.message + '，请刷新后重试',
            })
            return
          }
          res.data.username = localStorage.getItem('username')
          sentence.result = res.data.result
          sentence.resultId = res.data.id
          sentence.results.push(res.data)
          sentence.labeled = true
          this.success(ind)
        }).catch(err => {
          console.log(err)
          this.$notify.error({
            title: '出错了',
            message: '出错了',
          })
        }).finally(() => {
          this.btnEndLoading()
        })
      }
    },
    labelItem (sentence) {
      var sentenceInfo = {
        user: this.userId,
        sentence: sentence.id,
        result: JSON.stringify(sentence.result),
      }
      return new Promise((resolve, reject) => {
        apiLabelItem(sentence.id, sentenceInfo).then((res) => {
          resolve(res)
        }).catch(err => this.handleErr(err, reject))
      })
    },
    updateItem (sentence) {
      var sentenceInfo = {
        user: this.userId,
        sentence: sentence.id,
        result: JSON.stringify(sentence.result),
      }
      return new Promise((resolve, reject) => {
        apiUpdateItem(sentence.id, sentence.resultId, sentenceInfo).then((res) => {
          resolve(res)
        }).catch(err => this.handleErr(err, reject))
      })
    },
    handleErr (err, reject) {
      console.log(err && err.response)
      try {
        this.$notify.error({
          title: '出错了',
          message: err.response.statusText,
        })
      } catch (e) {
        this.$notify.error({
          title: '出错了',
          message: '请刷新后重试',
        })
      }
      reject(err && err.response)
    },
  },
}
