import axios from 'axios'
let base = 'http://127.0.0.1:8000/auth_api/api-token-auth/'
let login_api= {
  me (data = {}) {
    return axios.post(base, data)
  },
}

export default login_api
