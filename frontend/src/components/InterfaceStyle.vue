<template>
  <el-dialog title="界面风格" :visible.sync="dialogTableVisible">
    <div class="">
      蓝色
    </div>
    <div class="">
      灰色
    </div>
  </el-dialog>
</template>

<script>
export default {
  name: 'InterfaceStyle',
  props: ['dialogTableVisible'],
  data () {
    return {

    }
  },
  methods: {

  },
}
</script>

<style scoped>

</style>
