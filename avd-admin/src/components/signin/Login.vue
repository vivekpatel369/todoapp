<script>
  import login_api from '@/services/user'
  import router from '@/router/index.js'
  export default {
    data: () => ({
      username: this.username,
      password: this.password,
      responseData: null
    }),
    components: {
      
    },
    methods : {
        onLogin (){
          login_api.me({'username': this.username, 'password': this.password}).then(res=>{
            this.responseData = res.data
            console.log(this.responseData)
            window.localStorage.setItem('token', this.responseData.token)
            router.push('/');
          }).catch(error=>{
            console.log("VIVEK", error);
          })
      }
    },
  }
</script>


<template>
  <v-layout row wrap>
    <v-flex class="login_card col-md-5 col-sm-8 col-xs-12">
      <v-card class="white">
        <v-card-text class="indigo--text headline">Login Page</v-card-text>
        <v-flex xs8 offset-xs2>
          <v-text-field
            name="input-1"
            label="User Name"
            v-model="username"
          ></v-text-field>
        </v-flex>
        <v-flex xs8 offset-xs2>
          <v-text-field
            name="input-1"
            label="Password"
            v-model="password"
          ></v-text-field>
        </v-flex>

        <v-flex xs8 offset-xs2>
          <v-btn outline class="indigo--text submit_btn" v-on:click="onLogin()">Login</v-btn>
        </v-flex>
      </v-card>
    </v-flex>
  </v-layout>
</template>
<style>
  .login_card {
    text-align: center;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
  .submit_btn{
    margin-bottom: 40px;
  }
  .input-group {
    /*padding: 10px 0;*/
  }
</style>
