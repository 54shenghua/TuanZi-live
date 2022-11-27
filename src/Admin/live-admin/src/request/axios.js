import axios from 'axios'
export const Axios = axios.create({
  baseURL: 'http://127.0.0.1:8000',
  timeout: 10000, // 如果请求数据超过10s,没响应，就不请求了
  headers: {
    'Content-Type': 'application/json'
  }
})
