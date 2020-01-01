<template>
  <ul class="layui-nav">
      <li class="layui-nav-item">
        <a href="">控制台<span class="layui-badge">9</span></a>
      </li>
      <li class="layui-nav-item">
        <a href="">个人中心<span class="layui-badge-dot"></span></a>
      </li>
      <li class="layui-nav-item">
        <a href=""><img src="//t.cn/RCzsdCq" class="layui-nav-img">我</a>
        <dl class="layui-nav-child">
          <dd><a href="javascript:;">修改信息</a></dd>
          <dd><a href="javascript:;">安全管理</a></dd>
          <dd><a href="javascript:;">退了</a></dd>
        </dl>
      </li>
    </ul>
</template>

<script>
import InterfaceStyle from './InterfaceStyle'

export default {
  name: 'BaseHeader',
  components: {
    InterfaceStyle,
  },
  data () {
    return {
      username: localStorage.getItem('username'),
      token: localStorage.getItem('token'),
      dialogTableVisible: false,
    }
  },
  computed: {
    isShowGoGack: function () {
      return this.$route.name === 'LabelPage'
    }
  },
  methods: {
    goBack () {
      this.$router.push({ name: 'TasksDashboard' })
    },
    handleCommand (command) {
      switch (command) {
        case 'logout':
          this.logout()
          break
        case 'interfaceStyle':
          this.showInterfaceStyleDialog()
          break
        default:
      }
    },
    logout () {
      // TODO 接口
      localStorage.removeItem('token')
      localStorage.removeItem('username')
      localStorage.removeItem('userId')
      this.$router.push({ name: 'LoginPage' })
    },
    showInterfaceStyleDialog () {
      this.dialogTableVisible = true
    },
  },
  created: function () {
    if (!this.token) this.$router.push({ name: 'LoginPage' })
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.header {
  height: 30px;
  line-height: 30px;
  text-align: right;
  font-size: 12px;
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.3);
}
.go-back {
  padding: 5px;
  font-size: 20px;
  float: left;
}
.go-back:hover {
  background-color: #ecf5ff;
  color: #66b1ff;
}
.username {
  -moz-user-select: none;
  -khtml-user-select: none;
  user-select: none;
}
</style>
