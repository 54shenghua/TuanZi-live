import { Axios } from './axios'
// export function applysendmsg (a, b, c, d) {
//   return Axios.post('/start', { index: a, obname: b, position: c, jointime: d }, { params: { token: localStorage.getItem('token') } })
// }
export function Start () {
  return Axios.post('/start')
}

export function Stop () {
  return Axios.post('/stop')
}
