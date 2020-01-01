import axios from 'axios'

axios.defaults.baseURL = process.env.NODE_ENV === 'production' ? '/' : 'http://localhost:8000'

axios.interceptors.request.use(config => {
  let token = localStorage.getItem('token')
  if (token) {
    config.headers.authorization = 'JWT ' + token
  }
  return config
}, err => {
  console.log(err)
  return Promise.reject(err)
})

axios.interceptors.response.use(res => res, err => {
  try {
    if (err.response.statusText === 'Unauthorized') {
      localStorage.setItem('token', '')
    }
  } catch (e) { }
  return Promise.reject(err)
})

// 搜索
export const apiSearch = (character, israndom) => axios.post('/api/search/', {character, israndom})

// 获取汉字列表
export const apiGetCharactersList = (currentPage, pageSize) => axios.get(`/api/characters/?page=${currentPage}&size=${pageSize}`)

// 获取项目列表
export const apiGetProjectsList = () => axios.get(`/api/projects/pager/?page=1&size=9999`)

// 标注未被标注过的
export const apiLabelItem = (sentenceId, itemInfo) => axios.post(`/api/user/sentences/${sentenceId}/result`, itemInfo)

// 更新标注过的
export const apiUpdateItem = (sentenceId, resultId, itemInfo) => axios.put(`/api/user/sentences/${sentenceId}/results/${resultId}`, itemInfo)
