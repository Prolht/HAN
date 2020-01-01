import axios from 'axios'

axios.defaults.baseURL = process.env.NODE_ENV === 'production' ? '/' : 'http://localhost:8000'
// 获取文字列表
export const getProjects = () => axios.get(`/character`)
// 搜索
export const getCecEntityTypes = () => axios.get(`/search`)
// character
export const getItems = () => (characterId) => axios.get(`/character/${characterId}`)

// 搜索
export const apiSearch = (character, israndom) => axios.post('/api/search/', {character, israndom})

// 获取汉字列表
export const apiGetCharactersList = (currentPage, pageSize) => axios.get(`/api/characters/?page=${currentPage}&size=${pageSize}`)
