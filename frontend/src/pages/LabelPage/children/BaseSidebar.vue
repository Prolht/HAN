<template>
  <div class="">
    <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
      <el-menu :default-openeds="['1']" @select="switchTask">
        <el-submenu index="1">
          <template slot="title"><i class="el-icon-message"></i>任务</template>
          <el-menu-item-group title="">
            <el-menu-item
              v-for="task in tasksList"
              :index="task.id.toString()"
              :key="task.id" class="menu-item">
              {{task.name}}
              <el-progress :percentage="70" status=""></el-progress>
            </el-menu-item>
          </el-menu-item-group>
        </el-submenu>
      </el-menu>
    </el-aside>
  </div>
</template>

<script>
import {apiGetTasksList} from '@/service/getData'

export default {
  name: 'BaseSidebar',
  props: ['userId'],
  data () {
    return {
      tasksList: [],
    }
  },
  methods: {
    switchTask (taskId) {
      if (this.isSentenceDirty()) {
        this.unsubmittedAlert(() => {
          this.taskId = taskId
          // 切换停掉之前未返回的 api
          this.getTasksList()
        }, () => {
          console.log(this)
        })
      } else {
        this.taskId = taskId
        // 切换停掉之前未返回的 api
        this.getTasksList()
      }
    },
    getTasksList () {
      apiGetTasksList(this.userId).then((res) => {
        this.tasksList = res.data
        console.log(this.tasksList)
        if (!this.tasksList[0]) return
        this.taskId = this.tasksList[0].id
        // this.getItemsList()
      }).catch((err) => {
        console.log(err)
      })
    },
  },
  mounted () {
    this.getTasksList()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
