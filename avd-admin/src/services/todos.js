import axios from 'axios'

let base = 'http://127.0.0.1:8000/'
let token = window.localStorage.getItem('token')
let todos_api = {
  getList() {
    return axios.get(base + 'todos/')
  },
  addItem(data = {}) {
    return axios.post(base + 'todos/', data)
  },
  deleteItem(data = {}) {
    console.log(data)
    return axios.delete(base + 'todos/' + data.id + '/')
  },
  updateItem(data = {}) {
    return axios.put(base + 'todos/' + data.id + '/', data)
  },
  getTodoList() {
    return axios.get(base + 'todoslist/', {
      headers: {
        "Authorization": 'Token ' + token
      }
    })
  }
}

export default todos_api
