<template>
  <div class="login">
    <div class="input-container">
      <span>用户名</span>
      <el-input
        class="input"
        type="text"
        placeholder="请输入内容"
        @keyup.enter.native="login"
        v-model="username">
      </el-input>
    </div>
    <div class="input-container">
      <span>密码</span>
      <el-input
        class="input"
        type="password"
        placeholder="请输入内容"
        @keyup.enter.native="login"
        v-model="password">
      </el-input>
    </div>
    <el-button class="submit-btn" type="primary" @click="login">登录</el-button>
  </div>
</template>

<script>
// import {apiAccountLogin} from '@/service/getData'

// export default {
//   name: 'LoginPage',
//   data () {
//     return {
//       username: '',
//       password: ''
//     }
//   },
//   methods: {
//     login () {
//       if (this.username === '') {
//         this.$notify.error({
//           title: '出错了',
//           message: '用户名为空',
//         })
//         return
//       }
//       if (this.password === '') {
//         this.$notify.error({
//           title: '出错了',
//           message: '密码为空',
//         })
//         return
//       }

//       apiAccountLogin(this.username, this.password).then((res) => {
//         localStorage.setItem('token', res.data.token)
//         localStorage.setItem('username', this.username)

//         if (this.$route.query.redirect) {
//           this.$router.push(this.$route.query.redirect)
//         } else {
//           this.$router.push({name: 'TasksDashboard'})
//         }
//       }).catch((err) => {
//         var message = '出错了'
//         try {
//           message = err.response.data.non_field_errors[0]
//           message = message === '无法使用提供的认证信息登录。' ? '用户名或密码错误' : message
//         } catch (e) {}
//         this.$notify.error({
//           title: '出错了',
//           message: message,
//         })
//       })
//     }
//   }
// }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .login {
    width: 100%;
    max-width: 300px;
    margin: 100px auto 0;
  }
  .input-container {
    margin: 10px 0;
  }
  .input-container > span {
    width: 40px;
    display: inline-block;
  }
  .input-container > .input {
    width: 250px;
  }
  .submit-btn {
    margin: 50px auto;
    display: block;
  }
</style>
