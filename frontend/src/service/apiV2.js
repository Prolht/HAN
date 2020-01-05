import axios from 'axios'

axios.defaults.baseURL = process.env.NODE_ENV === 'production' ? 'http://localhost:8000/han' : 'http://localhost:8000'
// 获取文字列表
export const apipostCharacter = (character) => axios.post(`api/character/`, {character})

// 每日一首诗
export const apigetPoem = () => axios.get(`/poem`)

// 搜索随机
// TODO实现随机展示
export const apiSearch = (character, israndom) => axios.post('/api/search/', {character, israndom})

// 获取汉字列表
export const apiGetCharactersList = (currentPage, pageSize) => axios.get(`/api/list/?page=${currentPage}&size=${pageSize}`)

// TODO实现随机展示
// export const apiUpload = (character, israndom) => axios.post('/api/upload/', {character, israndom})
