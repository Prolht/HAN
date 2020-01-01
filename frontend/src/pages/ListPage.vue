<template>
  <div class="">
      <base-header></base-header>
      <div class="other"></div>
      <el-main class="main-container" v-loading="loading">
        <div>
          <el-table
            ref="multipleTable"
             :data="tableData.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))"
            tooltip-effect="dark"
            stripe="true"
            max-height="500"
            style="width: 100%"
            @selection-change="handleSelectionChange">
          <el-table-column
            type="index"
            label="序号"
            width="100">
          </el-table-column>
          <el-table-column
            prop="simplified"
            label="简体"
            width="300">
          </el-table-column>
          <el-table-column
            prop="traditional"
            label="繁体"
            width="300">
          </el-table-column>
          <el-table-column
            align="right">
            <template slot-scope="scope">
              <el-button
                size="mini"
                @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
            </template>
          </el-table-column>
          </el-table>
          <div style="text-align: center;margin-top: 30px;">
            <div class="block">
            <el-pagination class="pagination"
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
          </div>
        </div>
      </el-main>
    </div>
</template>

<script>
import {apiGetCharactersList} from '@/service/apiV2'
// import BaseHeader from '@/components/BaseHeader'

export default {
  name: 'ListPage',
  data () {
    return {
      currentPage: parseInt(this.$route.params.currentPage),
      pageSize: parseInt(this.$route.params.pageSize),
      simplified: '',
      tableData: [],
      search: '',
      multipleSelection: [],
      total: 2,
      isMobile: false,
      totalItems: this.currentPage * this.pageSize,
      // totalItems : 2,
    }
  },
  methods: {
    /**
     * 重置数据
     */
    resetData () {
      this.tableData = []
    },

    // 获取文字列表
    getTasksList () {
      this.loading = true
      apiGetCharactersList(this.currentPage, this.pageSize).then((res) => {
        this.loading = false
        this.tableData = res.data
      }).catch((err) => {
        console.log(err && err.response)
      })
    },

    handleEdit () {},
    handleSizeChange (pageSize) {
      this.pageSize = pageSize
      this.currentPage = 1
      this.getTasksList()
    },
    handleCurrentChange (currentPage) {
      this.currentPage = currentPage
      this.getTasksList()
    },

    handleSelectionChange () {
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
  },
  // created: function () {
  //   this.pageSize = 5
  //   this.currentPage = 1
  //   this.getTasksList()
  // },
  mounted: function () {
    this.pageSize = 5
    this.currentPage = 1
    this.getTasksList()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .other {
    height: 150px;
  }
  .main-container {
    width: 100%;
    max-width: 1200px;
    margin: 1px auto 0;
  }
  .table-text-blue{
  color: rgb(3, 3, 5);
  cursor:pointer;
  }
  .table-text-gray{
    color: #9132eb;
  }
  .el-table th.is-leaf{
    background: #9132eb;
    border-bottom: none;
  }
  .el-table--border th{
    border-color:#FFF;
    font-weight: normal;
  }
  .el-table--border{
    border:none;
  }
  .el-table,.el-table thead{
    color:rgb(5, 3, 7);
  }
  .el-table--border::after, .el-table--group::after{
    background-color: #fff;
  }
  .el-table th, .el-table tr {
    background-color: transparent;
    }
</style>
