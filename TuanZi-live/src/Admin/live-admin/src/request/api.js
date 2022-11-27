import Axios from './axios'
// export function applysendmsg (a, b, c, d) {
//   return Axios.post('/start', { index: a, obname: b, position: c, jointime: d }, { params: { token: localStorage.getItem('token') } })
// }
export function Start() {
  return Axios.post('/start')
}
export function Stop() {
  return Axios.post('/stop')
}
export function Submit(t, p, o) {
  return Axios.post('/inPutOptions', { time: t, problem: p, options: o }, { params: { key: values } })
}
export function Reset() {
  return Axios.post('/reset')
}

export function Preset(n) {
  return Axios.post('/getPreset', { index: n }, { params: { key: values } })
}
