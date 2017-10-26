import axios from 'axios'
let base = 'http://127.0.0.1:8000/todos/'
let todos_api= {
  getList () {
    return axios.get(base)
  },
  addItem (data = {}) {
    return axios.post(base, data)
  },
  deleteItem (data = {}) {
      console.log(data)
    return axios.delete(base+ data.id+'/')
  },
  updateItem (data = {}) {
    return axios.put(base+ data.id+'/', data)
  },
}

export default todos_api
